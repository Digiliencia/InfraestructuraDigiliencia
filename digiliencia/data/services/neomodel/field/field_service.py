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

        Raises:
            ValueError: If name is empty or None
        """
        if not name or not name.strip():
            raise ValueError("Field name cannot be empty")

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

    def get_all(self) -> List[Field]:
        """
        Get all fields.

        Returns:
            List[Field]: List of all fields
        """
        return list(Field.nodes.all())

    def get_subfields(self, field: str | Field | None = None) -> List[Field]:
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

    def get_fields(self) -> List[Field]:
        """
        Get all parent fields. Optional filter by field name or Field instance.

        Args:
            field: Field name or Field instance to get parent fields from

        Returns:
            List[Field]: List of parent fields
        """

        # Get all parent fields (fields that have subfields) in one query
        query = """
        MATCH (parent:Field)<-[:SUBFIELD_OF]-(subfield:Field)
        RETURN DISTINCT parent
        """
        results, _ = db.cypher_query(query)

        parent_fields = []
        for row in results:
            parent_field = Field.inflate(row[0])
            parent_fields.append(parent_field)

        return parent_fields

    def get_fields_hierarchy(self) -> str:
        """
        Get the hierarchy of fields.

        Returns:
            str: A string representation of the fields hierarchy

        Example:
            "Field1:
                - Subfield1
                - Subfield2
            Field2:
                - Subfield3
            "
        """
        fields = self.get_fields()
        hierarchy = []

        for field in fields:
            subfields = self.get_subfields(field)
            subfield_names = [str(subfield.name) for subfield in subfields]
            if subfield_names:
                hierarchy.append(
                    f"{field.name}:\n    - " + "\n    - ".join(subfield_names)
                )
            else:
                hierarchy.append(f"{field.name}:")

        return "\n".join(hierarchy)
