class DummyResult:
    def single(self):
        return None


class DummySession:
    def run(self, *args, **kwargs):
        return DummyResult()


class DummyContextManager:
    def __enter__(self):
        return DummySession()

    def __exit__(self, exc_type, exc_val, exc_tb):
        return None


class DummyContext:
    def __enter__(self):
        return DummySession()

    def __exit__(self, exc_type, exc_val, exc_tb):
        return None
