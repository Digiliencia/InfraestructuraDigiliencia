from dataclasses import dataclass

from digiliencia.data.models.interface_model import IModel


@dataclass(frozen=True)
class PersonModel(IModel):
    """Represents a person in the database."""

    id: str
    name: str
    email: str
    description: str
