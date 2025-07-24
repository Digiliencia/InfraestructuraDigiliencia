class FieldClassificationPrompt:
    """Generates hallucination-resistant prompts for subfield classification."""

    @staticmethod
    def generate_news_classification_prompt(
        fields: str, text: str, max_fields: int = 5
    ) -> str:
        return f"""
You are a careful classification assistant.

Your task is to identify which specific **sub-fields** the following news article directly and clearly relates to.
Sub-fields are classified under specific fields. You must only choose from the provided list of sub-fields, not general ones.

🛑 You MUST choose only from the sub-fields listed below.
🛑 Do NOT guess or invent new fields or sub-fields.
🛑 If the article is not clearly relevant to any, return an empty list: `[]`.
🛑 There is a maximum of {max_fields} sub-fields to choose from.

🧩 Fields and sub-fields (choose from this exact list):
{fields}

📰 News Article:
\"\"\"{text}\"\"\"

📤 Output rules:
- Return a JSON array with **only the exact names** of matching sub-fields.
- Do not include explanations or summaries.
- Do not include any sub-field not in the list above.
- If no sub-field clearly applies, return: []

✅ Example (valid):
["Data Protection", "Identity Management"]

❌ Example (invalid):
["Security", "General Tech"] ← Not in list

Remember: no explanation, no formatting — just a JSON list of sub-fields from the list above.
"""
