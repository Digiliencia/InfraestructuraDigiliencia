from enum import Enum


class AccessMode(Enum):
    """Enum for access modes in the database."""

    READ = "READ"
    WRITE = "WRITE"
