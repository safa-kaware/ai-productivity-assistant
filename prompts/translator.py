# prompts/translator.py

def build_translation_prompt(text: str, source_lang: str, target_lang: str) -> str:
    """
    Builds the prompt for the Translator tool.
    """
    return f"""You are a professional translator.

Translate the following text from {source_lang} to {target_lang}.

Structure your response using these exact section headers:

### Translation
(The primary, natural translation)

### Alternative Translation
(One alternative natural phrasing, if genuinely different and useful. If there isn't a meaningfully different alternative, write "Not applicable")

### Language Notes
(Only include this section if there's something a learner should know — idioms, tone shifts, cultural nuance, or ambiguity. If nothing notable, write "Not applicable")

Rules:
- Do not over-explain basic/simple translations.
- Preserve tone and formality level of the original text.

Text:
\"\"\"
{text}
\"\"\"
"""