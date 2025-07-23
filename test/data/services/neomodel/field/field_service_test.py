import pytest
from neomodel import db
from typing import List, Tuple

from digiliencia.data.models.neomodel.field import Field
from digiliencia.data.services.neomodel.field.field_service import FieldService


# Helper functions to apply DRY principle
def create_subfield_relationship(child_name: str, parent_name: str) -> None:
    """Helper function to create a subfield relationship using Cypher query."""
    db.cypher_query(
        """
        MATCH (child:Field {name: $child_name}), (parent:Field {name: $parent_name})
        CREATE (child)-[:SUBFIELD_OF]->(parent)
        """,
        {"child_name": child_name, "parent_name": parent_name},
    )


def create_multiple_relationships(relationships: List[Tuple[str, str]]) -> None:
    """Helper function to create multiple subfield relationships."""
    for child_name, parent_name in relationships:
        create_subfield_relationship(child_name, parent_name)


def create_field_hierarchy(
    field_service: FieldService, hierarchy_data: dict
) -> List[Field]:
    """
    Helper function to create a field hierarchy from configuration data.

    Args:
        field_service: The field service instance
        hierarchy_data: Dict with format {"parent_name": [child_names...]}

    Returns:
        List of all created fields
    """
    created_fields = []
    relationships = []

    for parent_name, children_data in hierarchy_data.items():
        # Extract parent description
        if isinstance(children_data, dict):
            parent_desc = children_data.get("description", f"{parent_name} field")
            children_names = children_data.get("children", [])
        else:
            parent_desc = f"{parent_name} field"
            children_names = children_data

        # Create parent field
        parent_field = field_service.create_field(parent_name, parent_desc)
        created_fields.append(parent_field)

        # Create child fields and track relationships
        for child_data in children_names:
            if isinstance(child_data, str):
                child_name = child_data
                child_desc = f"{child_name} field"
            else:
                child_name = child_data["name"]
                child_desc = child_data.get("description", f"{child_name} field")

            child_field = field_service.create_field(child_name, child_desc)
            created_fields.append(child_field)
            relationships.append((child_name, parent_name))

    # Create all relationships
    create_multiple_relationships(relationships)
    return created_fields


def verify_field_properties(
    field: Field, expected_name: str, expected_desc: str | None = None
) -> None:
    """Helper function to verify basic field properties."""
    assert isinstance(field, Field)
    assert field.name == expected_name
    if expected_desc is not None:
        assert field.description == expected_desc
    assert field.uid is not None


def verify_subfield_list(subfields: List[Field], expected_names: List[str]) -> None:
    """Helper function to verify a list of subfields contains expected names."""
    assert isinstance(subfields, list)
    assert len(subfields) == len(expected_names)
    subfield_names = [field.name for field in subfields]
    for expected_name in expected_names:
        assert expected_name in subfield_names


def verify_parent_field_list(
    parent_fields: List[Field], expected_names: List[str]
) -> None:
    """Helper function to verify a list of parent fields contains expected names."""
    assert isinstance(parent_fields, list)
    assert len(parent_fields) == len(expected_names)
    parent_names = [field.name for field in parent_fields]
    for expected_name in expected_names:
        assert expected_name in parent_names


def test_create_field_with_description(field_service: FieldService):
    """Test creating a field with name and description."""
    field = field_service.create_field(
        "Cybersecurity", "Field focused on protecting digital systems"
    )
    verify_field_properties(
        field, "Cybersecurity", "Field focused on protecting digital systems"
    )


def test_create_field_without_description(field_service: FieldService):
    """Test creating a field with only name (empty description)."""
    field = field_service.create_field("Data Science")
    verify_field_properties(field, "Data Science", "")


def test_create_duplicate_field_returns_existing(field_service: FieldService):
    """Test creating a duplicate field returns the existing one."""
    field1 = field_service.create_field(
        "Artificial Intelligence", "AI field description"
    )
    field2 = field_service.create_field(
        "Artificial Intelligence", "Different description"
    )

    # Should return the same field (first one created)
    assert field1.uid == field2.uid
    assert field1.description == "AI field description"  # Original preserved
    assert field2.description == "AI field description"  # Not overwritten


def test_get_field_by_name_existing(field_service: FieldService):
    """Test retrieving an existing field by name."""
    created_field = field_service.create_field(
        "Machine Learning", "ML field description"
    )
    retrieved_field = field_service.get_field_by_name("Machine Learning")

    assert retrieved_field is not None
    assert retrieved_field.uid == created_field.uid
    assert retrieved_field.name == created_field.name
    assert retrieved_field.description == created_field.description


def test_get_field_by_name_nonexistent(field_service: FieldService):
    """Test retrieving a nonexistent field returns None."""
    field = field_service.get_field_by_name("Nonexistent Field")
    assert field is None


def test_get_all_fields_empty(field_service: FieldService):
    """Test retrieving all fields when database is empty."""
    all_fields = field_service.get_all()
    assert isinstance(all_fields, list)
    assert len(all_fields) == 0


def test_get_all_fields_with_data(field_service: FieldService):
    """Test retrieving all fields with existing data."""
    initial_count = len(field_service.get_all())

    field_service.create_field("Computer Science", "CS description")
    field_service.create_field("Software Engineering", "SE description")

    all_fields = field_service.get_all()
    assert len(all_fields) >= initial_count + 2

    # Verify our fields are in the results
    field_names = [field.name for field in all_fields]
    assert "Computer Science" in field_names
    assert "Software Engineering" in field_names


def test_get_subfields_no_filter_empty_database(field_service: FieldService):
    """Test getting all subfields when database is empty."""
    subfields = field_service.get_subfields(None)
    assert isinstance(subfields, list)
    assert len(subfields) == 0


def test_get_subfields_no_filter_no_subfields(field_service: FieldService):
    """Test getting all subfields when no subfield relationships exist."""
    # Create fields but no relationships
    field_service.create_field("Field A", "Description A")
    field_service.create_field("Field B", "Description B")

    subfields = field_service.get_subfields(None)
    assert isinstance(subfields, list)
    assert len(subfields) == 0


def test_get_subfields_with_relationships(field_service: FieldService):
    """Test getting all subfields when subfield relationships exist."""
    # Use helper to create hierarchy
    hierarchy_data = {"Technology": ["AI", "Blockchain"]}
    create_field_hierarchy(field_service, hierarchy_data)

    subfields = field_service.get_subfields(None)
    verify_subfield_list(subfields, ["AI", "Blockchain"])


def test_get_subfields_by_field_name_existing(field_service: FieldService):
    """Test getting subfields by parent field name (existing field)."""
    # Use helper to create hierarchy
    hierarchy_data = {"Mathematics": ["Statistics"]}
    create_field_hierarchy(field_service, hierarchy_data)

    subfields = field_service.get_subfields("Mathematics")
    verify_subfield_list(subfields, ["Statistics"])


def test_get_subfields_by_field_name_nonexistent(field_service: FieldService):
    """Test getting subfields by nonexistent parent field name."""
    subfields = field_service.get_subfields("Nonexistent Field")
    assert isinstance(subfields, list)
    assert len(subfields) == 0


def test_get_subfields_by_field_instance(field_service: FieldService):
    """Test getting subfields by parent Field instance."""
    # Create parent and child fields
    parent_field = field_service.create_field("Physics", "Physics parent")
    child_field = field_service.create_field("Quantum Physics", "QP subfield")

    # Create relationship using helper
    create_subfield_relationship("Quantum Physics", "Physics")

    subfields = field_service.get_subfields(parent_field)
    verify_subfield_list(subfields, ["Quantum Physics"])


def test_get_subfields_by_field_with_no_children(field_service: FieldService):
    """Test getting subfields for a field that has no children."""
    parent_field = field_service.create_field("Chemistry", "Chemistry field")

    subfields = field_service.get_subfields(parent_field)
    assert isinstance(subfields, list)
    assert len(subfields) == 0


def test_get_subfields_multiple_levels(field_service: FieldService):
    """Test getting subfields with multiple hierarchy levels."""
    # Create a three-level hierarchy
    grandparent = field_service.create_field("Science", "Science field")
    parent = field_service.create_field("Biology", "Biology field")
    child = field_service.create_field("Genetics", "Genetics field")

    # Create relationships using helper
    relationships = [("Biology", "Science"), ("Genetics", "Biology")]
    create_multiple_relationships(relationships)

    # Test getting subfields of grandparent (should only return direct children)
    subfields = field_service.get_subfields(grandparent)
    verify_subfield_list(subfields, ["Biology"])

    # Test getting subfields of parent
    subfields = field_service.get_subfields(parent)
    verify_subfield_list(subfields, ["Genetics"])


def test_get_subfields_mixed_field_types(field_service: FieldService):
    """Test getting subfields with mixed field input types."""
    # Create fields
    parent_field = field_service.create_field("Engineering", "Engineering field")
    child_field = field_service.create_field("Software Engineering", "SE field")

    # Create relationship using helper
    create_subfield_relationship("Software Engineering", "Engineering")

    # Test with Field instance
    subfields_by_instance = field_service.get_subfields(parent_field)

    # Test with string name
    subfields_by_name = field_service.get_subfields("Engineering")

    # Both should return the same results
    assert len(subfields_by_instance) == len(subfields_by_name) == 1
    assert (
        subfields_by_instance[0].name
        == subfields_by_name[0].name
        == "Software Engineering"
    )


def test_get_subfields_database_error_handling(
    field_service: FieldService, monkeypatch
):
    """Test error handling in get_subfields method."""

    # Mock database error using monkeypatch
    def mock_cypher_query(*args, **kwargs):
        raise Exception("Database connection error")

    monkeypatch.setattr(
        "digiliencia.data.services.neomodel.field.field_service.db.cypher_query",
        mock_cypher_query,
    )

    # Should propagate the exception
    with pytest.raises(Exception, match="Database connection error"):
        field_service.get_subfields(None)


def test_field_service_initialization(monkeypatch):
    """Test FieldService initialization."""
    mock_config_called = False

    def mock_configure_neomodel():
        nonlocal mock_config_called
        mock_config_called = True

    monkeypatch.setattr(
        "digiliencia.data.services.neomodel.field.field_service.configure_neomodel",
        mock_configure_neomodel,
    )

    service = FieldService()
    assert mock_config_called
    assert isinstance(service, FieldService)


def test_create_field_empty_name_raises_error(field_service: FieldService):
    """Test that creating a field with empty name raises an error."""
    with pytest.raises(ValueError, match="Field name cannot be empty"):
        field_service.create_field("", "Some description")

    # Test with whitespace-only name
    with pytest.raises(ValueError, match="Field name cannot be empty"):
        field_service.create_field("   ", "Some description")

    # Test with None name (though type hints suggest this shouldn't happen)
    with pytest.raises(ValueError, match="Field name cannot be empty"):
        field_service.create_field(None, "Some description")  # type: ignore


def test_field_persistence(field_service: FieldService):
    """Test that created fields persist in the database."""
    # Create a field
    field = field_service.create_field("Persistence Test", "Test description")
    field_uid = field.uid

    # Create a new service instance to test persistence
    new_service = FieldService()
    retrieved_field = new_service.get_field_by_name("Persistence Test")

    assert retrieved_field is not None
    assert retrieved_field.uid == field_uid
    assert retrieved_field.name == "Persistence Test"
    assert retrieved_field.description == "Test description"


def test_subfield_relationship_integrity(field_service: FieldService):
    """Test the integrity of subfield relationships."""
    # Create fields
    parent = field_service.create_field("Parent Field", "Parent description")
    child = field_service.create_field("Child Field", "Child description")

    # Create relationship using helper
    create_subfield_relationship("Child Field", "Parent Field")

    # Verify relationship exists
    subfields = field_service.get_subfields(parent)
    assert len(subfields) == 1
    assert subfields[0].uid == child.uid

    # Verify reverse relationship using cypher query
    result, _ = db.cypher_query(
        """
        MATCH (child:Field {name: $child_name})-[:SUBFIELD_OF]->(parent:Field {name: $parent_name})
        RETURN count(*) as count
        """,
        {"child_name": "Child Field", "parent_name": "Parent Field"},
    )
    assert result[0][0] == 1  # Should find exactly one relationship


def test_get_subfields_performance_with_large_dataset(field_service: FieldService):
    """Test performance and correctness with multiple fields and relationships."""
    # Create multiple parent-child relationships using helper
    hierarchy_data = {
        "Technology": [f"Tech Subfield {i}" for i in range(3)],
        "Science": [f"Science Subfield {i}" for i in range(3)],
    }
    create_field_hierarchy(field_service, hierarchy_data)

    # Test getting subfields for specific parents
    tech_subfields = field_service.get_subfields("Technology")
    science_subfields = field_service.get_subfields("Science")

    verify_subfield_list(tech_subfields, [f"Tech Subfield {i}" for i in range(3)])
    verify_subfield_list(science_subfields, [f"Science Subfield {i}" for i in range(3)])

    # Test getting all subfields
    all_subfields = field_service.get_subfields(None)
    assert len(all_subfields) >= 6  # At least our 6 subfields


def test_create_field_with_special_characters(field_service: FieldService):
    """Test creating fields with special characters in name and description."""
    field = field_service.create_field(
        "AI & Machine Learning",
        "Field covering AI, ML, and related technologies (including NLP, CV, etc.)",
    )

    assert field.name == "AI & Machine Learning"
    assert "AI, ML" in str(field.description)
    assert field.uid is not None

    # Verify retrieval works with special characters
    retrieved = field_service.get_field_by_name("AI & Machine Learning")
    assert retrieved is not None
    assert retrieved.uid == field.uid


def test_field_service_concurrent_access(field_service: FieldService):
    """Test that field service handles concurrent-like access patterns."""
    # Simulate concurrent creation of the same field
    field1 = field_service.create_field("Concurrent Test", "First call")
    field2 = field_service.create_field("Concurrent Test", "Second call")

    # Should return the same field instance
    assert field1.uid == field2.uid
    assert field1.description == "First call"  # Original description preserved

    # Verify only one field exists in database
    all_fields = field_service.get_all()
    concurrent_fields = [f for f in all_fields if f.name == "Concurrent Test"]
    assert len(concurrent_fields) == 1


def test_get_fields_empty_database(field_service: FieldService):
    """Test getting all parent fields when database is empty."""
    parent_fields = field_service.get_fields()
    assert isinstance(parent_fields, list)
    assert len(parent_fields) == 0


def test_get_fields_no_relationships(field_service: FieldService):
    """Test getting parent fields when no subfield relationships exist."""
    # Create fields but no relationships
    field_service.create_field("Standalone Field A", "Description A")
    field_service.create_field("Standalone Field B", "Description B")

    parent_fields = field_service.get_fields()
    assert isinstance(parent_fields, list)
    assert len(parent_fields) == 0


def test_get_fields_with_relationships(field_service: FieldService):
    """Test getting parent fields when subfield relationships exist."""
    # Use helper to create hierarchy
    hierarchy_data = {
        "Computer Science": ["Algorithms", "Data Structures"],
        "Mathematics": ["Statistics"],
    }
    create_field_hierarchy(field_service, hierarchy_data)

    parent_fields = field_service.get_fields()
    verify_parent_field_list(parent_fields, ["Computer Science", "Mathematics"])


def test_get_fields_multiple_levels_hierarchy(field_service: FieldService):
    """Test getting parent fields with multiple hierarchy levels."""
    # Create a three-level hierarchy
    grandparent = field_service.create_field("Science", "Science field")
    parent = field_service.create_field("Biology", "Biology field")
    child = field_service.create_field("Genetics", "Genetics field")

    # Create relationships using helper
    relationships = [("Biology", "Science"), ("Genetics", "Biology")]
    create_multiple_relationships(relationships)

    parent_fields = field_service.get_fields()
    parent_names = [field.name for field in parent_fields]

    # Should include both Science and Biology as they both have subfields
    assert "Science" in parent_names
    assert "Biology" in parent_names
    assert len(parent_fields) >= 2


def test_get_fields_database_error_handling(field_service: FieldService, monkeypatch):
    """Test error handling in get_fields method."""

    # Mock database error using monkeypatch
    def mock_cypher_query(*args, **kwargs):
        raise Exception("Database connection error")

    monkeypatch.setattr(
        "digiliencia.data.services.neomodel.field.field_service.db.cypher_query",
        mock_cypher_query,
    )

    # Should propagate the exception
    with pytest.raises(Exception, match="Database connection error"):
        field_service.get_fields()


def test_get_fields_hierarchy_empty_database(field_service: FieldService):
    """Test getting fields hierarchy when database is empty."""
    hierarchy = field_service.get_fields_hierarchy()
    assert isinstance(hierarchy, str)
    assert hierarchy == ""


def test_get_fields_hierarchy_no_relationships(field_service: FieldService):
    """Test getting fields hierarchy when no subfield relationships exist."""
    # Create fields but no relationships
    field_service.create_field("Standalone Field", "Description")

    hierarchy = field_service.get_fields_hierarchy()
    assert isinstance(hierarchy, str)
    assert hierarchy == ""


def test_get_fields_hierarchy_with_relationships(field_service: FieldService):
    """Test getting fields hierarchy with subfield relationships."""
    # Use helper to create hierarchy
    hierarchy_data = {"Technology": ["AI", "Blockchain"]}
    create_field_hierarchy(field_service, hierarchy_data)

    hierarchy = field_service.get_fields_hierarchy()
    assert isinstance(hierarchy, str)
    assert "Technology:" in hierarchy
    assert "AI" in hierarchy
    assert "Blockchain" in hierarchy
    # Should contain the subfield formatting
    assert "    - " in hierarchy


def test_get_fields_hierarchy_multiple_parents(field_service: FieldService):
    """Test getting fields hierarchy with multiple parent fields."""
    # Use helper to create hierarchy
    hierarchy_data = {
        "Engineering": ["Software Engineering"],
        "Mathematics": ["Statistics", "Calculus"],
    }
    create_field_hierarchy(field_service, hierarchy_data)

    hierarchy = field_service.get_fields_hierarchy()
    assert isinstance(hierarchy, str)

    # Should contain both parent fields
    assert "Engineering:" in hierarchy
    assert "Mathematics:" in hierarchy

    # Should contain their respective subfields
    assert "Software Engineering" in hierarchy
    assert "Statistics" in hierarchy
    assert "Calculus" in hierarchy


def test_get_fields_hierarchy_mixed_with_and_without_subfields(
    field_service: FieldService,
):
    """Test hierarchy generation when some parent fields have no subfields."""
    # Use helper to create hierarchy
    hierarchy_data = {"Technology": ["AI"]}
    create_field_hierarchy(field_service, hierarchy_data)

    hierarchy = field_service.get_fields_hierarchy()
    assert isinstance(hierarchy, str)
    assert "Technology:" in hierarchy
    assert "AI" in hierarchy


def test_get_fields_hierarchy_format_consistency(field_service: FieldService):
    """Test that hierarchy format is consistent and properly formatted."""
    # Use helper to create hierarchy
    hierarchy_data = {"Science": ["Physics", "Chemistry"]}
    create_field_hierarchy(field_service, hierarchy_data)

    hierarchy = field_service.get_fields_hierarchy()

    # Should have proper formatting
    lines = hierarchy.split("\n")
    assert any("Science:" in line for line in lines)

    # Check for proper indentation in subfields
    subfield_lines = [line for line in lines if "    - " in line]
    assert len(subfield_lines) >= 2

    # Verify actual subfield names are present
    subfield_text = "\n".join(subfield_lines)
    assert "Physics" in subfield_text
    assert "Chemistry" in subfield_text


def test_get_fields_hierarchy_parent_without_subfields_edge_case(
    field_service: FieldService, monkeypatch
):
    """Test hierarchy generation when get_fields returns a field but get_subfields returns empty (edge case)."""
    # Use helper to create hierarchy
    hierarchy_data = {"Test Parent": ["Test Child"]}
    create_field_hierarchy(field_service, hierarchy_data)

    # Mock get_subfields to return empty list for specific field to trigger else clause
    original_get_subfields = field_service.get_subfields

    def mock_get_subfields(field):
        if hasattr(field, "name") and field.name == "Test Parent":
            return []  # Force empty subfields for this parent
        return original_get_subfields(field)

    monkeypatch.setattr(field_service, "get_subfields", mock_get_subfields)

    hierarchy = field_service.get_fields_hierarchy()

    # Should contain the parent field name with colon but no subfields
    assert "Test Parent:" in hierarchy
    # Should not contain the subfield indentation for this field
    lines = hierarchy.split("\n")
    parent_line_found = False
    for line in lines:
        if "Test Parent:" in line and line.strip() == "Test Parent:":
            parent_line_found = True
            break
    assert parent_line_found
