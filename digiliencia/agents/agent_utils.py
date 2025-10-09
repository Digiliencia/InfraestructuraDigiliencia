"""
Utility functions and configuration management for the agent system.

This module provides shared utilities, configuration classes, and helper
functions used across all agents.
"""

import time
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

from loguru import logger


@dataclass
class AgentConfig:
    """
    Configuration class for agent initialization.
    
    Centralizes all agent configuration parameters.
    """
    model_name: str = "llama3.1:8b"
    temperature: float = 0.7
    verbose: bool = False
    max_iterations: int = 10
    timeout_seconds: float = 600.0  # 10 minutos para sistemas lentos
    request_timeout: float = 600.0  # 10 minutos para sistemas lentos
    
    def __post_init__(self):
        """Validate configuration after initialization."""
        if self.temperature < 0.0 or self.temperature > 1.0:
            logger.warning(f"Temperature {self.temperature} outside recommended range [0.0, 1.0]")
        
        if self.max_iterations < 1:
            logger.warning(f"max_iterations {self.max_iterations} too low, setting to 1")
            self.max_iterations = 1
        
        if self.timeout_seconds < 10:
            logger.warning(f"timeout_seconds {self.timeout_seconds} too low, setting to 10")
            self.timeout_seconds = 10


@dataclass
class PerformanceMetrics:
    """
    Data class for tracking agent performance metrics.
    """
    total_requests: int = 0
    successful_requests: int = 0
    failed_requests: int = 0
    total_response_time: float = 0.0
    min_response_time: float = float('inf')
    max_response_time: float = 0.0
    agent_type: str = "unknown"
    
    def record_request(self, success: bool, response_time: float):
        """
        Record a request's metrics.
        
        Args:
            success: Whether the request was successful
            response_time: Time taken for the request in seconds
        """
        self.total_requests += 1
        
        if success:
            self.successful_requests += 1
        else:
            self.failed_requests += 1
        
        self.total_response_time += response_time
        self.min_response_time = min(self.min_response_time, response_time)
        self.max_response_time = max(self.max_response_time, response_time)
    
    def get_average_response_time(self) -> float:
        """Get average response time in seconds."""
        if self.total_requests == 0:
            return 0.0
        return self.total_response_time / self.total_requests
    
    def get_success_rate(self) -> float:
        """Get success rate as a percentage."""
        if self.total_requests == 0:
            return 0.0
        return (self.successful_requests / self.total_requests) * 100
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert metrics to dictionary format."""
        return {
            "agent_type": self.agent_type,
            "total_requests": self.total_requests,
            "successful_requests": self.successful_requests,
            "failed_requests": self.failed_requests,
            "success_rate": round(self.get_success_rate(), 2),
            "average_response_time": round(self.get_average_response_time(), 2),
            "min_response_time": round(self.min_response_time, 2) if self.min_response_time != float('inf') else 0.0,
            "max_response_time": round(self.max_response_time, 2),
        }


class PerformanceMonitor:
    """
    Singleton class for monitoring agent performance across the system.
    """
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        if self._initialized:
            return
        
        self._metrics: Dict[str, PerformanceMetrics] = {}
        self._start_time = time.time()
        self._initialized = True
        logger.debug("PerformanceMonitor initialized")
    
    def record_request(
        self,
        agent_type: str,
        response_time: float,
        success: bool = True,
    ):
        """
        Record a request's performance metrics.
        
        Args:
            agent_type: Type of agent that handled the request
            response_time: Time taken in seconds
            success: Whether the request was successful
        """
        if agent_type not in self._metrics:
            self._metrics[agent_type] = PerformanceMetrics(agent_type=agent_type)
        
        self._metrics[agent_type].record_request(success, response_time)
        logger.debug(f"Recorded request for {agent_type}: {response_time:.2f}s, success={success}")
    
    def get_metrics(self, agent_type: Optional[str] = None) -> Dict[str, Any]:
        """
        Get performance metrics.
        
        Args:
            agent_type: Specific agent type (None = all agents)
            
        Returns:
            Dictionary with performance metrics
        """
        if agent_type and agent_type in self._metrics:
            return self._metrics[agent_type].to_dict()
        
        # Return aggregated metrics for all agents
        total_requests = sum(m.total_requests for m in self._metrics.values())
        total_successful = sum(m.successful_requests for m in self._metrics.values())
        total_failed = sum(m.failed_requests for m in self._metrics.values())
        total_time = sum(m.total_response_time for m in self._metrics.values())
        
        uptime_seconds = time.time() - self._start_time
        requests_per_minute = (total_requests / uptime_seconds * 60) if uptime_seconds > 0 else 0
        
        return {
            "total_requests": total_requests,
            "successful_requests": total_successful,
            "failed_requests": total_failed,
            "success_rate": round((total_successful / total_requests * 100) if total_requests > 0 else 0.0, 2),
            "average_response_time": round((total_time / total_requests) if total_requests > 0 else 0.0, 2),
            "uptime_seconds": round(uptime_seconds, 2),
            "requests_per_minute": round(requests_per_minute, 2),
            "agent_metrics": {
                agent_type: metrics.to_dict()
                for agent_type, metrics in self._metrics.items()
            },
        }
    
    def reset_metrics(self, agent_type: Optional[str] = None):
        """
        Reset performance metrics.
        
        Args:
            agent_type: Specific agent type (None = reset all)
        """
        if agent_type and agent_type in self._metrics:
            self._metrics[agent_type] = PerformanceMetrics(agent_type=agent_type)
            logger.debug(f"Reset metrics for {agent_type}")
        else:
            self._metrics.clear()
            self._start_time = time.time()
            logger.debug("Reset all metrics")


def get_performance_monitor() -> PerformanceMonitor:
    """
    Get the singleton PerformanceMonitor instance.
    
    Returns:
        PerformanceMonitor instance
    """
    return PerformanceMonitor()


def validate_config(config: AgentConfig) -> List[str]:
    """
    Validate agent configuration and return any issues.
    
    Args:
        config: AgentConfig instance to validate
        
    Returns:
        List of validation messages (empty if no issues)
    """
    issues = []
    
    if config.temperature < 0.0 or config.temperature > 2.0:
        issues.append(
            f"WARNING: Temperature {config.temperature} is outside typical range [0.0, 2.0]"
        )
    
    if config.max_iterations < 1 or config.max_iterations > 50:
        issues.append(
            f"WARNING: max_iterations {config.max_iterations} is outside recommended range [1, 50]"
        )
    
    if config.timeout_seconds < 10:
        issues.append(
            f"WARNING: timeout_seconds {config.timeout_seconds} is very low and may cause failures"
        )
    
    if config.request_timeout < 30:
        issues.append(
            f"WARNING: request_timeout {config.request_timeout} is low for complex queries"
        )
    
    if not config.model_name:
        issues.append("ERROR: model_name cannot be empty")
    
    return issues


def format_query_context(
    query: str,
    max_length: int = 500,
    include_metadata: bool = False,
) -> str:
    """
    Format a query for logging or display.
    
    Args:
        query: The query to format
        max_length: Maximum length before truncation
        include_metadata: Whether to include metadata
        
    Returns:
        Formatted query string
    """
    formatted = query.strip()
    
    if len(formatted) > max_length:
        formatted = formatted[:max_length] + "..."
    
    if include_metadata:
        formatted = f"[Length: {len(query)}] {formatted}"
    
    return formatted


def sanitize_agent_response(response: str) -> str:
    """
    Sanitize agent response for safe display.
    
    Args:
        response: Raw agent response
        
    Returns:
        Sanitized response string
    """
    # Remove any potential script tags or dangerous content
    sanitized = response.replace("<script>", "").replace("</script>", "")
    
    # Ensure response is not empty
    if not sanitized.strip():
        sanitized = "I apologize, but I couldn't generate a proper response. Please try again."
    
    return sanitized.strip()
