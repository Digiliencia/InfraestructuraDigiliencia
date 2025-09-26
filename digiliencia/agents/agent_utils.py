"""
Configuration and utility functions for the improved agent system.
Provides centralized configuration management and helper functions.
"""

import json
import time
from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict, List, Optional


class LogLevel(Enum):
    """Logging levels for the agent system."""

    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"


@dataclass
class AgentConfig:
    """Configuration class for agent system."""

    # Model configuration
    model_name: str = "llama3.2:3b"
    conversational_temperature: float = 0.2
    tool_calling_temperature: float = 0.0

    # Performance limits
    max_iterations: int = 5
    timeout_seconds: int = 180
    memory_token_limit: int = 10000
    max_history_messages: int = 20

    # Logging configuration
    log_level: LogLevel = LogLevel.INFO
    verbose: bool = False

    # Tool configuration
    enable_parallel_tools: bool = False
    max_concurrent_tools: int = 3

    # Safety and reliability
    max_retries: int = 2
    enable_fallback: bool = True
    rate_limit_requests_per_minute: int = 60


class PerformanceMonitor:
    """Monitor and track agent performance metrics."""

    def __init__(self):
        self.metrics = {
            "total_requests": 0,
            "total_errors": 0,
            "total_response_time": 0.0,
            "average_response_time": 0.0,
            "error_rate": 0.0,
            "requests_per_minute": 0.0,
            "start_time": time.time(),
            "agent_usage": {},
            "tool_usage": {},
            "error_types": {},
        }
        self.request_timestamps = []

    def record_request(
        self,
        agent_type: str,
        response_time: float,
        success: bool,
        error_type: Optional[str] = None,
    ):
        """Record a request for performance tracking."""
        current_time = time.time()

        # Update basic metrics
        self.metrics["total_requests"] += 1
        self.metrics["total_response_time"] += response_time
        self.metrics["average_response_time"] = (
            self.metrics["total_response_time"] / self.metrics["total_requests"]
        )

        if not success:
            self.metrics["total_errors"] += 1
            if error_type:
                self.metrics["error_types"][error_type] = (
                    self.metrics["error_types"].get(error_type, 0) + 1
                )

        self.metrics["error_rate"] = (
            self.metrics["total_errors"] / self.metrics["total_requests"]
        ) * 100

        # Track agent usage
        self.metrics["agent_usage"][agent_type] = (
            self.metrics["agent_usage"].get(agent_type, 0) + 1
        )

        # Track request rate (requests per minute)
        self.request_timestamps.append(current_time)
        # Keep only timestamps from the last minute
        minute_ago = current_time - 60
        self.request_timestamps = [
            ts for ts in self.request_timestamps if ts > minute_ago
        ]
        self.metrics["requests_per_minute"] = len(self.request_timestamps)

    def record_tool_usage(self, tool_name: str, execution_time: float, success: bool):
        """Record tool usage for monitoring."""
        if tool_name not in self.metrics["tool_usage"]:
            self.metrics["tool_usage"][tool_name] = {
                "count": 0,
                "total_time": 0.0,
                "errors": 0,
                "average_time": 0.0,
            }

        tool_stats = self.metrics["tool_usage"][tool_name]
        tool_stats["count"] += 1
        tool_stats["total_time"] += execution_time
        tool_stats["average_time"] = tool_stats["total_time"] / tool_stats["count"]

        if not success:
            tool_stats["errors"] += 1

    def get_metrics(self) -> Dict[str, Any]:
        """Get current performance metrics."""
        uptime = time.time() - self.metrics["start_time"]

        # Calculate additional derived metrics
        derived_metrics = {
            "uptime_seconds": uptime,
            "uptime_hours": uptime / 3600,
            "requests_per_hour": (
                self.metrics["total_requests"] / max(uptime / 3600, 0.01)
            ),
            "success_rate": 100 - self.metrics["error_rate"],
            "most_used_agent": (
                max(self.metrics["agent_usage"], key=self.metrics["agent_usage"].get)
                if self.metrics["agent_usage"]
                else None
            ),
            "most_used_tool": (
                max(
                    self.metrics["tool_usage"],
                    key=lambda k: self.metrics["tool_usage"][k]["count"],
                )
                if self.metrics["tool_usage"]
                else None
            ),
        }

        return {**self.metrics, **derived_metrics}

    def reset_metrics(self):
        """Reset all performance metrics."""
        self.__init__()

    def export_metrics(self, filepath: str):
        """Export metrics to a JSON file."""
        metrics = self.get_metrics()
        with open(filepath, "w") as f:
            json.dump(metrics, f, indent=2, default=str)


class CircuitBreaker:
    """Simple circuit breaker for agent reliability."""

    def __init__(self, failure_threshold: int = 5, recovery_timeout: int = 60):
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.failure_count = 0
        self.last_failure_time = None
        self.state = "CLOSED"  # CLOSED, OPEN, HALF_OPEN

    def call(self, func, *args, **kwargs):
        """Call a function through the circuit breaker."""
        if self.state == "OPEN":
            if time.time() - self.last_failure_time > self.recovery_timeout:  # type: ignore
                self.state = "HALF_OPEN"
            else:
                raise Exception("Circuit breaker is OPEN - too many recent failures")

        try:
            result = func(*args, **kwargs)

            if self.state == "HALF_OPEN":
                self.state = "CLOSED"
                self.failure_count = 0

            return result

        except Exception as e:
            self.failure_count += 1
            self.last_failure_time = time.time()

            if self.failure_count >= self.failure_threshold:
                self.state = "OPEN"

            raise e

    def reset(self):
        """Reset the circuit breaker."""
        self.failure_count = 0
        self.last_failure_time = None
        self.state = "CLOSED"


class RateLimiter:
    """Simple rate limiter for API calls."""

    def __init__(self, max_requests_per_minute: int = 60):
        self.max_requests = max_requests_per_minute
        self.requests = []

    def is_allowed(self) -> bool:
        """Check if a request is allowed based on rate limiting."""
        current_time = time.time()

        # Remove requests older than 1 minute
        minute_ago = current_time - 60
        self.requests = [
            req_time for req_time in self.requests if req_time > minute_ago
        ]

        # Check if under limit
        if len(self.requests) < self.max_requests:
            self.requests.append(current_time)
            return True

        return False

    def time_until_next_request(self) -> float:
        """Get time in seconds until next request is allowed."""
        if not self.requests:
            return 0.0

        oldest_request = min(self.requests)
        return max(0.0, 60 - (time.time() - oldest_request))


def validate_config(config: AgentConfig) -> List[str]:
    """
    Validate agent configuration and return list of warnings/errors.

    Args:
        config: Agent configuration to validate

    Returns:
        List of validation messages
    """
    issues = []

    # Check model name
    if not config.model_name:
        issues.append("ERROR: Model name cannot be empty")

    # Check temperature ranges
    if not (0.0 <= config.conversational_temperature <= 1.0):
        issues.append(
            "WARNING: Conversational temperature should be between 0.0 and 1.0"
        )

    if not (0.0 <= config.tool_calling_temperature <= 1.0):
        issues.append("WARNING: Tool calling temperature should be between 0.0 and 1.0")

    # Check performance limits
    if config.max_iterations < 1:
        issues.append("ERROR: max_iterations must be at least 1")

    if config.timeout_seconds < 10:
        issues.append(
            "WARNING: timeout_seconds is very low, may cause premature timeouts"
        )

    if config.memory_token_limit < 1000:
        issues.append(
            "WARNING: memory_token_limit is very low, may limit conversation context"
        )

    # Check safety limits
    if config.max_retries < 0:
        issues.append("ERROR: max_retries cannot be negative")

    if config.rate_limit_requests_per_minute < 1:
        issues.append("ERROR: rate_limit_requests_per_minute must be at least 1")

    return issues


def create_default_config() -> AgentConfig:
    """Create a default configuration with sensible defaults."""
    return AgentConfig()


def load_config_from_file(filepath: str) -> AgentConfig:
    """
    Load configuration from a JSON file.

    Args:
        filepath: Path to configuration file

    Returns:
        Loaded configuration
    """
    try:
        with open(filepath, "r") as f:
            data = json.load(f)

        # Convert log level string to enum
        if "log_level" in data:
            data["log_level"] = LogLevel(data["log_level"])

        return AgentConfig(**data)

    except Exception as e:
        raise ValueError(f"Failed to load configuration from {filepath}: {e}")


def save_config_to_file(config: AgentConfig, filepath: str):
    """
    Save configuration to a JSON file.

    Args:
        config: Configuration to save
        filepath: Path to save configuration
    """
    # Convert to dictionary
    config_dict = {
        field.name: getattr(config, field.name)
        for field in config.__dataclass_fields__.values()
    }

    # Convert enum to string
    if "log_level" in config_dict:
        config_dict["log_level"] = config_dict["log_level"].value

    with open(filepath, "w") as f:
        json.dump(config_dict, f, indent=2)


# Global performance monitor instance
global_performance_monitor = PerformanceMonitor()


def get_performance_monitor() -> PerformanceMonitor:
    """Get the global performance monitor instance."""
    return global_performance_monitor
