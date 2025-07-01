"""Author service for managing authors using neomodel."""

from typing import List, Optional

from digiliencia.data.models.neomodel.person.author import Author
from digiliencia.data.services.neomodel.config import configure_neomodel


class AuthorService:
    """Service for managing authors using neomodel."""

    def __init__(self) -> None:
        """Initialize the author service."""
        configure_neomodel()

    def create_author(
        self, name: str, email: str = "", description: str = ""
    ) -> Author:
        """
        Create an author.

        Args:
            name: Author name
            email: Author email
            description: Author description

        Returns:
            Author: The created author instance
        """
        try:
            return Author.nodes.get(name=name)
        except Author.DoesNotExist:
            return Author(name=name, email=email, description=description).save()

    def get_author_by_name(self, name: str) -> Optional[Author]:
        """
        Get an author by name.

        Args:
            name: Author name

        Returns:
            Author: The author instance or None if not found
        """
        try:
            return Author.nodes.get(name=name)
        except Author.DoesNotExist:
            return None

    def get_all_authors(self) -> List[Author]:
        """
        Get all authors.

        Returns:
            List[Author]: List of all authors
        """
        return list(Author.nodes.all())
