from digiliencia.data.models.neomodel.person.author import Author
from digiliencia.data.services.neomodel.author_service import AuthorService


def test_create_author(author_service: AuthorService):
    """Test creating an author."""
    author = author_service.create_author(
        "Test Author", "test@example.com", "Test author description"
    )

    assert isinstance(author, Author)
    assert author.name == "Test Author"
    assert author.email == "test@example.com"
    assert author.description == "Test author description"


def test_get_nonexistent_author(author_service: AuthorService):
    """Test retrieving nonexistent author."""
    author = author_service.get_author_by_name("Nonexistent Author")
    assert author is None


def test_create_duplicate_author(author_service: AuthorService):
    """Test creating a duplicate author returns existing one."""
    author1 = author_service.create_author("Duplicate Author", "first@example.com")
    author2 = author_service.create_author("Duplicate Author", "second@example.com")

    # Should return the same author (first one created)
    assert author1.uid == author2.uid
    assert author1.email == "first@example.com"  # Original email preserved


def test_create_author_minimal(author_service: AuthorService):
    """Test creating an author with minimal information."""
    author = author_service.create_author("Minimal Author")

    assert isinstance(author, Author)
    assert author.name == "Minimal Author"
    assert author.email == ""
    assert author.description == ""


def test_get_author_by_name(author_service: AuthorService):
    """Test retrieving author by name."""
    created_author = author_service.create_author(
        "Searchable Author", "search@example.com"
    )
    retrieved_author = author_service.get_author_by_name("Searchable Author")

    assert retrieved_author is not None
    assert retrieved_author.uid == created_author.uid
    assert retrieved_author.name == created_author.name
    assert retrieved_author.email == created_author.email


def test_get_all_authors(author_service: AuthorService):
    """Test retrieving all authors."""
    initial_count = len(author_service.get_all_authors())

    author_service.create_author("Author X", "x@example.com")
    author_service.create_author("Author Y", "y@example.com")

    all_authors = author_service.get_all_authors()
    assert len(all_authors) >= initial_count + 2

    # Verify our authors are in the results
    author_names = [author.name for author in all_authors]
    assert "Author X" in author_names
    assert "Author Y" in author_names
