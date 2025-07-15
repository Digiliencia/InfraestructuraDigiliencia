"""Data models for the classification microservice."""

from typing import List, Optional
from pydantic import BaseModel, Field


class TopicCandidate(BaseModel):
    """Model for a topic candidate."""

    name: str = Field(..., description="Name of the topic")
    definition: str = Field(..., description="Definition of the topic")


class ClassificationRequest(BaseModel):
    """Model for classification request."""

    text: str = Field(..., description="Text to classify", min_length=1)
    headline: Optional[str] = Field(None, description="Optional headline of the text")
    topic_candidates: List[TopicCandidate] = Field(
        ..., description="List of possible topics to classify into", min_length=1
    )
    max_topics: int = Field(
        default=5, description="Maximum number of topics to return", ge=1, le=20
    )
    confidence_threshold: float = Field(
        default=0.1, description="Minimum confidence score for topic inclusion", ge=0.0, le=1.0
    )


class TopicResult(BaseModel):
    """Model for a classified topic result."""

    name: str = Field(..., description="Name of the classified topic")
    confidence: float = Field(..., description="Confidence score", ge=0.0, le=1.0)


class ClassificationResponse(BaseModel):
    """Model for classification response."""

    topics: List[TopicResult] = Field(..., description="List of classified topics")
    processing_time_ms: float = Field(..., description="Processing time in milliseconds")


class HealthResponse(BaseModel):
    """Model for health check response."""

    status: str = Field(..., description="Service status")
    model_loaded: bool = Field(..., description="Whether the model is loaded")
    version: str = Field(..., description="Service version")
