"""FastAPI application for text classification microservice."""

from contextlib import asynccontextmanager
from typing import Dict, Any

from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger
import sys

from models import ClassificationRequest, ClassificationResponse, HealthResponse
from classification_service import TextClassificationService

# Configure logging
logger.remove()
logger.add(
    sys.stdout,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
    level="INFO",
)
logger.add(
    "logs/classification_service.log",
    rotation="100 MB",
    retention="30 days",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}",
    level="INFO",
)

# Global classification service instance
classification_service: TextClassificationService | None = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Manage application lifespan events."""
    global classification_service

    # Startup
    logger.info("Starting Classification Microservice...")
    try:
        classification_service = TextClassificationService()
        logger.info("Classification service initialized successfully")
    except Exception as e:
        logger.error(f"Failed to initialize classification service: {e}")
        raise

    yield

    # Shutdown
    logger.info("Shutting down Classification Microservice...")


# Create FastAPI app
app = FastAPI(
    title="Text Classification Microservice",
    description="A microservice for classifying cybersecurity news using RoBERTa-large-mnli",
    version="1.0.0",
    lifespan=lifespan,
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", response_model=Dict[str, str])
async def root() -> Dict[str, str]:
    """Root endpoint."""
    return {"message": "Text Classification Microservice", "version": "1.0.0", "status": "running"}


@app.get("/health", response_model=HealthResponse)
async def health_check() -> HealthResponse:
    """Health check endpoint."""
    global classification_service

    return HealthResponse(
        status="healthy"
        if classification_service and classification_service.is_model_loaded()
        else "unhealthy",
        model_loaded=classification_service.is_model_loaded() if classification_service else False,
        version="1.0.0",
    )


@app.get("/model-info", response_model=Dict[str, Any])
async def get_model_info() -> Dict[str, Any]:
    """Get information about the loaded model."""
    global classification_service

    if not classification_service:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Classification service not initialized",
        )

    return classification_service.get_model_info()


@app.post("/classify", response_model=ClassificationResponse)
async def classify_text(request: ClassificationRequest) -> ClassificationResponse:
    """
    Classify text into cybersecurity topics.

    Args:
        request: Classification request containing text and topic candidates

    Returns:
        ClassificationResponse: Classification results with confidence scores
    """
    global classification_service

    if not classification_service:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Classification service not initialized",
        )

    if not classification_service.is_model_loaded():
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Classification model not loaded",
        )

    try:
        logger.info(
            f"Received classification request for text with {len(request.topic_candidates)} "
            f"candidate topics, max_topics: {request.max_topics}"
        )

        topics, processing_time = classification_service.classify_text(
            text=request.text,
            headline=request.headline or "",
            topic_candidates=request.topic_candidates,
            max_topics=request.max_topics,
            confidence_threshold=request.confidence_threshold,
        )

        logger.info(f"Classification completed, returning {len(topics)} topics")

        return ClassificationResponse(topics=topics, processing_time_ms=processing_time)

    except RuntimeError as e:
        logger.error(f"Classification runtime error: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    except Exception as e:
        logger.error(f"Unexpected error during classification: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error during classification",
        )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True, log_level="info")
