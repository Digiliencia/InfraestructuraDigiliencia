from typing import Dict, List

from digiliencia.agents.prompts.field_classification_prompt import \
    FieldClassificationPrompt
from digiliencia.data.models.neomodel.field import Field
from digiliencia.data.services.neomodel.base_classification_service import \
    BaseClassificationService
from digiliencia.data.services.neomodel.field.field_service import FieldService


class FieldClassificationService(BaseClassificationService[Field]):
    def _initialize_data(self) -> None:
        """Initialize field-specific data."""
        self.field_service = FieldService()
        self.fields = self.field_service.get_all()
        self.fields_hierarchy = self.field_service.get_fields_hierarchy()

    def _generate_prompt(self, text: str, max_items: int) -> str:
        """Generate field classification prompt."""
        return FieldClassificationPrompt.generate_news_classification_prompt(
            fields=self.fields_hierarchy, text=text, max_fields=max_items
        )

    def _get_name_to_object_mapping(self) -> Dict[str, Field]:
        """Get mapping from field names to Field objects."""
        return {str(f.name): f for f in self.fields}

    def _get_entity_type_name(self) -> str:
        """Get entity type name for logging."""
        return "field"

    def classify_news_fields(self, news, max_fields: int = 10) -> List[Field]:
        """
        Classify news content into fields.

        Args:
            news: News object containing content to classify
            max_fields: Maximum number of fields to return

        Returns:
            List of classified Field objects
        """
        return self.classify_news(news, max_fields)
