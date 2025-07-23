from typing import List, Optional

from neomodel import db

from digiliencia.data.models.neomodel.field import Field
from digiliencia.data.services.neomodel.config import configure_neomodel


class FieldService:
    """Service for managing fields using neomodel."""

    def __init__(self) -> None:
        """Initialize the field service."""
        configure_neomodel()

    def create_field(self, name: str, description: str = "") -> Field:
        """
        Create a field.

        Args:
            name: Field name
            description: Field description

        Returns:
            Field: The created field instance
        """
        try:
            return Field.nodes.get(name=name)
        except Field.DoesNotExist:
            return Field(name=name, description=description).save()

    def get_field_by_name(self, name: str) -> Optional[Field]:
        """
        Get a field by name.

        Args:
            name: Field name

        Returns:
            Field: The field instance or None if not found
        """
        try:
            return Field.nodes.get(name=name)
        except Field.DoesNotExist:
            return None

    def get_all_fields(self) -> List[Field]:
        """
        Get all fields.

        Returns:
            List[Field]: List of all fields
        """
        return list(Field.nodes.all())
    
    def get_subfields(self, field: str | Field | None) -> List[Field]:
        """
        Get all subfields. Optional filter by field name or Field instance.

        Args:
            field: Field name or Field instance

        Returns:
            List[Field]: List of subfields
        """
        # Get the field instance if provided
        field_instance = None
        if field:
            if isinstance(field, Field):
                field_instance = field
            elif isinstance(field, str):
                field_instance = self.get_field_by_name(field)
                if not field_instance:
                    return []  # Field not found
        
        # Single query to get all fields and filter in one pass
        if field_instance is None:
            # Get all subfields (fields that have a parent field) in one query
            query = """
            MATCH (subfield:Field)-[:SUBFIELD_OF]->(parent:Field)
            RETURN subfield
            """
            results, _ = db.cypher_query(query)
            
            subfields = []
            for row in results:
                subfield = Field.inflate(row[0])
                subfields.append(subfield)
        else:
            # Get subfields of the specific field in one query
            query = """
            MATCH (subfield:Field)-[:SUBFIELD_OF]->(parent:Field)
            WHERE parent.uid = $parent_uid
            RETURN subfield
            """
            results, _ = db.cypher_query(query, {"parent_uid": field_instance.uid})
            
            subfields = []
            for row in results:
                subfield = Field.inflate(row[0])
                subfields.append(subfield)
        
        return subfields
            
