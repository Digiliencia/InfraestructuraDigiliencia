"""Service focused on Chunk creation and embeddings backfill for News content."""

import gc
import os
from typing import Iterable, List, Optional

import requests
from loguru import logger

from digiliencia.data.models.neomodel.chunk import Chunk
from digiliencia.data.models.neomodel.news import News


class ChunkService:
    def _split_text_into_chunks(
        self,
        text: str,
        max_chars: int = 800,
        overlap: int = 100,
        preserve_newlines: bool = True,
    ) -> List[str]:
        if not text:
            return []
        s = text if preserve_newlines else " ".join(text.split())
        chunks: List[str] = []
        start = 0
        n = len(s)
        if max_chars <= 0:
            max_chars = 800
        if overlap < 0:
            overlap = 0
        while start < n:
            end = min(n, start + max_chars)
            if preserve_newlines and end < n:
                window = s[start:end]
                cut = window.rfind("\n")
                if cut == -1:
                    cut = window.rfind(". ")
                if cut == -1:
                    cut = window.rfind(" ")
                if cut != -1 and cut > max(0, len(window) - 120):
                    end = start + cut + 1
            chunks.append(s[start:end].strip())
            if end == n:
                break
            start = max(0, end - overlap)
        return [c for c in chunks if c]

    def _batch(self, items: Iterable[str], size: int) -> Iterable[List[str]]:
        buf: List[str] = []
        for it in items:
            buf.append(it)
            if len(buf) >= size:
                yield buf
                buf = []
        if buf:
            yield buf

    def generate_chunk_embeddings_for_news(
        self,
        news: News,
        *,
        kind: str = "content",
        chunk_size: int = 800,
        overlap: int = 100,
        batch_size: int = 16,
        include_header: bool = True,
        force_regenerate: bool = False,
    ) -> int:
        embeddings_service_url = os.getenv("EMBEDDINGS_SERVICE")
        if not embeddings_service_url:
            logger.error("EMBEDDINGS_SERVICE environment variable not set")
            return 0

        texts: List[str] = []
        mapping: List[tuple[int, str]] = []  # (index, kind)

        idx = 0
        if include_header and news.header:
            texts.append(str(news.header))
            mapping.append((idx, "header"))
            idx += 1

        for piece in self._split_text_into_chunks(
            str(news.content or ""), max_chars=chunk_size, overlap=overlap
        ):
            texts.append(piece)
            mapping.append((idx, kind))
            idx += 1

        if not texts:
            return 0

        created = 0
        if force_regenerate:
            try:
                for ch in news.chunks.all():  # type: ignore[attr-defined]
                    try:
                        news.chunks.disconnect(ch)  # type: ignore[attr-defined]
                    except Exception:
                        pass
                    try:
                        ch.delete()
                    except Exception:
                        pass
            except Exception:
                pass

        with requests.Session() as session:
            session.headers.update({"Content-Type": "application/json"})
            all_vectors: List[List[float]] = []
            # cap batch size to maximum 30 per request
            effective_bs = max(1, min(int(batch_size) if batch_size else 16, 30))
            for batch in self._batch(texts, effective_bs):
                try:
                    resp = session.post(embeddings_service_url, json={"texts": batch})
                    resp.raise_for_status()
                    vecs = resp.json().get("embeddings") or []
                    all_vectors.extend(vecs)
                except Exception as e:
                    logger.error(
                        f"Chunk embedding batch failed for news {news.uid}: {str(e)[:120]}"
                    )
                    break
                finally:
                    gc.collect()

        if len(all_vectors) != len(texts):
            logger.warning(
                f"Embeddings count mismatch for news {news.uid}: got {len(all_vectors)} for {len(texts)} texts"
            )

        for i, (idx, k) in enumerate(mapping):
            text = texts[i]
            emb = all_vectors[i] if i < len(all_vectors) else None

            existing = None
            if not force_regenerate:
                try:
                    existing_list = news.chunks.filter(index=idx, text=text)  # type: ignore[attr-defined]
                    existing = existing_list[0] if existing_list else None
                except Exception:
                    existing = None

            if existing:
                if emb is not None:
                    existing.embedding = emb
                    existing.save()
                try:
                    news.chunks.connect(existing)  # type: ignore[attr-defined]
                except Exception:
                    pass
            else:
                c = Chunk(index=idx, text=text, embedding=emb, kind=k).save()
                try:
                    news.chunks.connect(c)  # type: ignore[attr-defined]
                except Exception:
                    pass
                created += 1

        news.save()
        return created

    def generate_chunks_for_all_news(
        self,
        limit: Optional[int] = None,
        *,
        only_missing: bool = True,
        chunk_size: int = 800,
        overlap: int = 100,
        include_header: bool = True,
        batch_size: int = 16,
    ) -> int:
        processed = 0
        for news in News.nodes.all():
            if limit is not None and processed >= limit:
                break
            try:
                if only_missing:
                    try:
                        existing_chunks = news.chunks.all()  # type: ignore[attr-defined]
                    except Exception:
                        existing_chunks = []
                    if existing_chunks:
                        continue

                created = self.generate_chunk_embeddings_for_news(
                    news,
                    kind="content",
                    chunk_size=chunk_size,
                    overlap=overlap,
                    batch_size=batch_size,
                    include_header=include_header,
                )
                if created > 0:
                    processed += 1
                    if processed % 5 == 0 or processed == 1:
                        logger.info(
                            f"Chunked {processed} news items (latest: {news.header[:50]}...)"
                        )
            except Exception as e:
                logger.error(
                    f"Failed chunking news {getattr(news, 'uid', '?')}: {str(e)[:120]}"
                )
            finally:
                gc.collect()
        logger.info(f"Chunk generation completed. News processed: {processed}")
        return processed

    def generate_embeddings_for_missing_chunks(
        self,
        limit: Optional[int] = None,
        batch_size: int = 32,
    ) -> int:
        embeddings_service_url = os.getenv("EMBEDDINGS_SERVICE")
        if not embeddings_service_url:
            logger.error("EMBEDDINGS_SERVICE environment variable not set")
            return 0

        updated = 0
        failed = 0
        buffer: List[Chunk] = []

        def _process_buffer(session: requests.Session, buf: List[Chunk]) -> int:
            nonlocal failed
            if not buf:
                return 0
            texts = [str(c.text or "") for c in buf]
            try:
                resp = session.post(embeddings_service_url, json={"texts": texts})
                resp.raise_for_status()
                vecs = resp.json().get("embeddings") or []
                if len(vecs) != len(buf):
                    logger.warning(
                        f"Embeddings count mismatch for chunk batch: got {len(vecs)} for {len(buf)} texts"
                    )
                count = 0
                for i, ch in enumerate(buf):
                    if i < len(vecs) and vecs[i] is not None:
                        try:
                            ch.embedding = vecs[i]
                            ch.save()
                            count += 1
                        except Exception as e:
                            failed += 1
                            logger.error(
                                f"Failed saving embedding for chunk {getattr(ch, 'uid', '?')}: {str(e)[:120]}"
                            )
                return count
            except Exception as e:
                failed += len(buf)
                logger.error(f"Failed embedding chunk batch: {str(e)[:150]}")
                return 0

        with requests.Session() as session:
            session.headers.update({"Content-Type": "application/json"})
            try:
                # cap batch size to maximum 30 per request
                effective_bs = max(1, min(int(batch_size) if batch_size else 32, 30))
                for ch in Chunk.nodes.filter(embedding__isnull=True):
                    if limit is not None and updated >= limit:
                        break
                    buffer.append(ch)
                    if len(buffer) >= effective_bs:
                        updated += _process_buffer(session, buffer)
                        buffer = []
                        gc.collect()

                if buffer and (limit is None or updated < limit):
                    updated += _process_buffer(session, buffer)
            finally:
                gc.collect()

        if updated > 0:
            logger.info(
                f"Chunk embedding backfill completed. Updated: {updated}, Failed: {failed}"
            )
        else:
            logger.info("No chunks found without embeddings")
        return updated
