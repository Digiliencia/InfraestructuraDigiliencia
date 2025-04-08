from dataclasses import dataclass
from abc import ABC
from digiliencia.data.models.interface_model import IModel


@dataclass(frozen=True)
class OrganizationModel(IModel, ABC):
    """Represents an organization in the database."""

    id: int
    name: str
    description: str
