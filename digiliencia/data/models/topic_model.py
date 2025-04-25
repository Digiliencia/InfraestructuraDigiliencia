from dataclasses import dataclass
from digiliencia.data.models.interface_model import IModel


@dataclass(frozen=True)
class TopicModel(IModel):
    """Represents a topic in the database."""

    id: str
    name: str
    definition: str
