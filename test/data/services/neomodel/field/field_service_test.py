import pytest
from neomodel import db

from digiliencia.data.models.neomodel.field import Field
from digiliencia.data.services.neomodel.field.field_service import FieldService


class TestFieldService:
    """Test cases for FieldService."""

    def test_create_field_with_description(self, field_service: FieldService):
        """Test creating a field with name and description."""
        field = field_service.create_field(
            "Cybersecurity", "Field focused on protecting digital systems"
        )

        assert isinstance(field, Field)
        assert field.name == "Cybersecurity"
        assert field.description == "Field focused on protecting digital systems"
        assert field.uid is not None

    def test_create_field_without_description(self, field_service: FieldService):
        """Test creating a field with only name (empty description)."""
        field = field_service.create_field("Data Science")

        assert isinstance(field, Field)
        assert field.name == "Data Science"
        assert field.description == ""
        assert field.uid is not None

    def test_create_duplicate_field_returns_existing(self, field_service: FieldService):
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

    def test_get_field_by_name_existing(self, field_service: FieldService):
        """Test retrieving an existing field by name."""
        created_field = field_service.create_field(
            "Machine Learning", "ML field description"
        )
        retrieved_field = field_service.get_field_by_name("Machine Learning")

        assert retrieved_field is not None
        assert retrieved_field.uid == created_field.uid
        assert retrieved_field.name == created_field.name
        assert retrieved_field.description == created_field.description

    def test_get_field_by_name_nonexistent(self, field_service: FieldService):
        """Test retrieving a nonexistent field returns None."""
        field = field_service.get_field_by_name("Nonexistent Field")
        assert field is None

    def test_get_all_fields_empty(self, field_service: FieldService):
        """Test retrieving all fields when database is empty."""
        all_fields = field_service.get_all_fields()
        assert isinstance(all_fields, list)
        assert len(all_fields) == 0

    def test_get_all_fields_with_data(self, field_service: FieldService):
        """Test retrieving all fields with existing data."""
        initial_count = len(field_service.get_all_fields())

        field_service.create_field("Computer Science", "CS description")
        field_service.create_field("Software Engineering", "SE description")

        all_fields = field_service.get_all_fields()
        assert len(all_fields) >= initial_count + 2

        # Verify our fields are in the results
        field_names = [field.name for field in all_fields]
        assert "Computer Science" in field_names
        assert "Software Engineering" in field_names

    def test_get_subfields_no_filter_empty_database(self, field_service: FieldService):
        """Test getting all subfields when database is empty."""
        subfields = field_service.get_subfields(None)
        assert isinstance(subfields, list)
        assert len(subfields) == 0

    def test_get_subfields_no_filter_no_subfields(self, field_service: FieldService):
        """Test getting all subfields when no subfield relationships exist."""
        # Create fields but no relationships
        field_service.create_field("Field A", "Description A")
        field_service.create_field("Field B", "Description B")

        subfields = field_service.get_subfields(None)
        assert isinstance(subfields, list)
        assert len(subfields) == 0

    def test_get_subfields_with_relationships(self, field_service: FieldService):
        """Test getting all subfields when subfield relationships exist."""
        # Create parent and child fields
        parent_field = field_service.create_field("Technology", "Parent field")
        child_field1 = field_service.create_field("AI", "AI subfield")
        child_field2 = field_service.create_field("Blockchain", "Blockchain subfield")

        # Create subfield relationships using cypher query to avoid linter issues
        db.cypher_query(
            """
            MATCH (child:Field {name: $child_name}), (parent:Field {name: $parent_name})
            CREATE (child)-[:SUBFIELD_OF]->(parent)
            """,
            {"child_name": "AI", "parent_name": "Technology"}
        )
        db.cypher_query(
            """
            MATCH (child:Field {name: $child_name}), (parent:Field {name: $parent_name})
            CREATE (child)-[:SUBFIELD_OF]->(parent)
            """,
            {"child_name": "Blockchain", "parent_name": "Technology"}
        )

        subfields = field_service.get_subfields(None)
        assert len(subfields) == 2
        subfield_names = [field.name for field in subfields]
        assert "AI" in subfield_names
        assert "Blockchain" in subfield_names

    def test_get_subfields_by_field_name_existing(self, field_service: FieldService):
        """Test getting subfields by parent field name (existing field)."""
        # Create parent and child fields
        parent_field = field_service.create_field("Mathematics", "Math parent")
        child_field = field_service.create_field("Statistics", "Stats subfield")

        # Create subfield relationship using cypher query
        db.cypher_query(
            """
            MATCH (child:Field {name: $child_name}), (parent:Field {name: $parent_name})
            CREATE (child)-[:SUBFIELD_OF]->(parent)
            """,
            {"child_name": "Statistics", "parent_name": "Mathematics"}
        )

        subfields = field_service.get_subfields("Mathematics")
        assert len(subfields) == 1
        assert subfields[0].name == "Statistics"

    def test_get_subfields_by_field_name_nonexistent(self, field_service: FieldService):
        """Test getting subfields by nonexistent parent field name."""
        subfields = field_service.get_subfields("Nonexistent Field")
        assert isinstance(subfields, list)
        assert len(subfields) == 0

    def test_get_subfields_by_field_instance(self, field_service: FieldService):
        """Test getting subfields by parent Field instance."""
        # Create parent and child fields
        parent_field = field_service.create_field("Physics", "Physics parent")
        child_field = field_service.create_field("Quantum Physics", "QP subfield")

        # Create subfield relationship using cypher query
        db.cypher_query(
            """
            MATCH (child:Field {name: $child_name}), (parent:Field {name: $parent_name})
            CREATE (child)-[:SUBFIELD_OF]->(parent)
            """,
            {"child_name": "Quantum Physics", "parent_name": "Physics"}
        )

        subfields = field_service.get_subfields(parent_field)
        assert len(subfields) == 1
        assert subfields[0].name == "Quantum Physics"

    def test_get_subfields_by_field_with_no_children(self, field_service: FieldService):
        """Test getting subfields for a field that has no children."""
        parent_field = field_service.create_field("Chemistry", "Chemistry field")

        subfields = field_service.get_subfields(parent_field)
        assert isinstance(subfields, list)
        assert len(subfields) == 0

    def test_get_subfields_multiple_levels(self, field_service: FieldService):
        """Test getting subfields with multiple hierarchy levels."""
        # Create a three-level hierarchy
        grandparent = field_service.create_field("Science", "Science field")
        parent = field_service.create_field("Biology", "Biology field")
        child = field_service.create_field("Genetics", "Genetics field")

        # Create relationships using cypher queries
        db.cypher_query(
            """
            MATCH (child:Field {name: $child_name}), (parent:Field {name: $parent_name})
            CREATE (child)-[:SUBFIELD_OF]->(parent)
            """,
            {"child_name": "Biology", "parent_name": "Science"}
        )
        db.cypher_query(
            """
            MATCH (child:Field {name: $child_name}), (parent:Field {name: $parent_name})
            CREATE (child)-[:SUBFIELD_OF]->(parent)
            """,
            {"child_name": "Genetics", "parent_name": "Biology"}
        )

        # Test getting subfields of grandparent (should only return direct children)
        subfields = field_service.get_subfields(grandparent)
        assert len(subfields) == 1
        assert subfields[0].name == "Biology"

        # Test getting subfields of parent
        subfields = field_service.get_subfields(parent)
        assert len(subfields) == 1
        assert subfields[0].name == "Genetics"

    def test_get_subfields_mixed_field_types(self, field_service: FieldService):
        """Test getting subfields with mixed field input types."""
        # Create fields
        parent_field = field_service.create_field("Engineering", "Engineering field")
        child_field = field_service.create_field("Software Engineering", "SE field")

        # Create relationship using cypher query
        db.cypher_query(
            """
            MATCH (child:Field {name: $child_name}), (parent:Field {name: $parent_name})
            CREATE (child)-[:SUBFIELD_OF]->(parent)
            """,
            {"child_name": "Software Engineering", "parent_name": "Engineering"}
        )

        # Test with Field instance
        subfields_by_instance = field_service.get_subfields(parent_field)
        
        # Test with string name
        subfields_by_name = field_service.get_subfields("Engineering")

        # Both should return the same results
        assert len(subfields_by_instance) == len(subfields_by_name) == 1
        assert subfields_by_instance[0].name == subfields_by_name[0].name == "Software Engineering"

    def test_get_subfields_database_error_handling(self, field_service: FieldService, monkeypatch):
        """Test error handling in get_subfields method."""
        # Mock database error using monkeypatch
        def mock_cypher_query(*args, **kwargs):
            raise Exception("Database connection error")
        
        monkeypatch.setattr("digiliencia.data.services.neomodel.field.field_service.db.cypher_query", mock_cypher_query)

        # Should propagate the exception
        with pytest.raises(Exception, match="Database connection error"):
            field_service.get_subfields(None)

    def test_field_service_initialization(self, monkeypatch):
        """Test FieldService initialization."""
        mock_config_called = False
        
        def mock_configure_neomodel():
            nonlocal mock_config_called
            mock_config_called = True
        
        monkeypatch.setattr("digiliencia.data.services.neomodel.field.field_service.configure_neomodel", mock_configure_neomodel)
        
        service = FieldService()
        assert mock_config_called
        assert isinstance(service, FieldService)

    def test_create_field_empty_name_raises_error(self, field_service: FieldService):
        """Test that creating a field with empty name raises an error."""
        with pytest.raises(ValueError, match="Field name cannot be empty"):
            field_service.create_field("", "Some description")
        
        # Test with whitespace-only name
        with pytest.raises(ValueError, match="Field name cannot be empty"):
            field_service.create_field("   ", "Some description")
        
        # Test with None name (though type hints suggest this shouldn't happen)
        with pytest.raises(ValueError, match="Field name cannot be empty"):
            field_service.create_field(None, "Some description")  # type: ignore

    def test_field_persistence(self, field_service: FieldService):
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

    def test_subfield_relationship_integrity(self, field_service: FieldService):
        """Test the integrity of subfield relationships."""
        # Create fields
        parent = field_service.create_field("Parent Field", "Parent description")
        child = field_service.create_field("Child Field", "Child description")

        # Create relationship using cypher query
        db.cypher_query(
            """
            MATCH (child:Field {name: $child_name}), (parent:Field {name: $parent_name})
            CREATE (child)-[:SUBFIELD_OF]->(parent)
            """,
            {"child_name": "Child Field", "parent_name": "Parent Field"}
        )

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
            {"child_name": "Child Field", "parent_name": "Parent Field"}
        )
        assert result[0][0] == 1  # Should find exactly one relationship

    def test_get_subfields_performance_with_large_dataset(self, field_service: FieldService):
        """Test performance and correctness with multiple fields and relationships."""
        # Create multiple parent fields
        parent1 = field_service.create_field("Technology", "Technology field")
        parent2 = field_service.create_field("Science", "Science field")
        
        # Create multiple child fields for each parent
        children_tech = []
        children_science = []
        
        for i in range(3):
            tech_child = field_service.create_field(f"Tech Subfield {i}", f"Tech description {i}")
            science_child = field_service.create_field(f"Science Subfield {i}", f"Science description {i}")
            children_tech.append(tech_child)
            children_science.append(science_child)
            
            # Create relationships
            db.cypher_query(
                """
                MATCH (child:Field {name: $child_name}), (parent:Field {name: $parent_name})
                CREATE (child)-[:SUBFIELD_OF]->(parent)
                """,
                {"child_name": f"Tech Subfield {i}", "parent_name": "Technology"}
            )
            db.cypher_query(
                """
                MATCH (child:Field {name: $child_name}), (parent:Field {name: $parent_name})
                CREATE (child)-[:SUBFIELD_OF]->(parent)
                """,
                {"child_name": f"Science Subfield {i}", "parent_name": "Science"}
            )

        # Test getting subfields for specific parents
        tech_subfields = field_service.get_subfields("Technology")
        science_subfields = field_service.get_subfields("Science")
        
        assert len(tech_subfields) == 3
        assert len(science_subfields) == 3
        
        # Test getting all subfields
        all_subfields = field_service.get_subfields(None)
        assert len(all_subfields) >= 6  # At least our 6 subfields
        
        # Verify field names
        tech_names = [field.name for field in tech_subfields]
        science_names = [field.name for field in science_subfields]
        
        for i in range(3):
            assert f"Tech Subfield {i}" in tech_names
            assert f"Science Subfield {i}" in science_names

    def test_create_field_with_special_characters(self, field_service: FieldService):
        """Test creating fields with special characters in name and description."""
        field = field_service.create_field(
            "AI & Machine Learning", 
            "Field covering AI, ML, and related technologies (including NLP, CV, etc.)"
        )
        
        assert field.name == "AI & Machine Learning"
        assert "AI, ML" in str(field.description)
        assert field.uid is not None
        
        # Verify retrieval works with special characters
        retrieved = field_service.get_field_by_name("AI & Machine Learning")
        assert retrieved is not None
        assert retrieved.uid == field.uid

    def test_field_service_concurrent_access(self, field_service: FieldService):
        """Test that field service handles concurrent-like access patterns."""
        # Simulate concurrent creation of the same field
        field1 = field_service.create_field("Concurrent Test", "First call")
        field2 = field_service.create_field("Concurrent Test", "Second call")
        
        # Should return the same field instance
        assert field1.uid == field2.uid
        assert field1.description == "First call"  # Original description preserved
        
        # Verify only one field exists in database
        all_fields = field_service.get_all_fields()
        concurrent_fields = [f for f in all_fields if f.name == "Concurrent Test"]
        assert len(concurrent_fields) == 1
