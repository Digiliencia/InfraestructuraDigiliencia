class FieldClassificationPrompt:
    """Handles prompt generation for field classification tasks."""

    @staticmethod
    def generate_news_classification_prompt(
        fields: str, text: str, max_fields: int = 10
    ) -> str:
        """
        Builds a system prompt that explains the task, provides a field-subfield hierarchy,
        and requests a clean JSON list of matching subtopics based on the article content.

        Args:
            fields: Field-subfield hierarchy as a string
            text: The news article content to classify
            max_fields: Maximum number of fields to return

        Returns:
            Formatted prompt string for the LLM
        """
        return f"""You are a topic classification assistant.

Your task is to classify a news article into a maximum of {max_fields} relevant **subtopics**, based on the provided hierarchy of topics and subtopics.

Do NOT include main topics. Only return subtopics (leaves of the hierarchy).

Available topics and subtopics:
{fields}

News content:
\"\"\"{text}\"\"\"

Output format:
Return only a valid JSON list (array) of subtopics, like this:
["Online Surveillance", "Data Protection", "Victims and Harms"]

Do not explain your answer.
Do not return anything other than the JSON list.
"""
