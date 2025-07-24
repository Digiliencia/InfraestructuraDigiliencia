class FieldClassificationPrompt:
    """Generates hallucination-resistant prompts for subfield classification."""

    @staticmethod
    def generate_news_classification_prompt(
        fields: str, text: str, max_fields: int = 5
    ) -> str:
        return f"""
You are a careful classification assistant.

Your task is to identify which specific **topics** the following news article directly and clearly relates to.
Topics are classified under specific fields. You must only choose from the provided list of topics, not general fields.

🛑 You MUST choose only from the topics listed below.
🛑 Do NOT guess or invent new fields or topics.
🛑 If the article is not clearly relevant to any, return an empty list: `[]`.
🛑 There is a maximum of {max_fields} topics to choose from.

🧩 Topics (choose from this exact list):
{fields}

📰 News Article:
\"\"\"{text}\"\"\"

📤 Output rules:
- Return a JSON array with **only the exact names** of matching topics.
- Do not include explanations or summaries.
- Do not include any topic not in the list above.
- If no topic clearly applies, return: []

✅ Example (valid):
["Data Protection", "Identity Management"]

❌ Example (invalid):
["Security", "General Tech"] ← Not in list

Remember: no explanation, no formatting — just a JSON list of topics from the list above.
"""
