from loguru import logger


class MetricsTracker:
    """Registra métricas de rendimiento para agentes."""

    def __init__(self):
        self.total_requests = 0
        self.total_errors = 0
        self.total_time = 0.0

    def log_request(self, elapsed: float, error: bool = False):
        """Registrar una petición completada."""
        self.total_requests += 1
        self.total_time += elapsed
        if error:
            self.total_errors += 1

    def report(self) -> dict:
        """Obtener resumen de métricas."""
        avg_time = self.total_time / max(self.total_requests, 1)
        error_rate = self.total_errors / max(self.total_requests, 1) * 100
        return {
            "requests": self.total_requests,
            "errors": self.total_errors,
            "avg_time": avg_time,
            "error_rate": error_rate,
        }

    def reset(self):
        """Reiniciar métricas."""
        logger.info("Reiniciando métricas")
        self.__init__()
