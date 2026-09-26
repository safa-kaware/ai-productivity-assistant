# prompts/email.py

def build_email_prompt(email_text: str, tone: str, length: str) -> str:
    """
    Builds the prompt for the Email Rewriter tool.
    tone: "Professional" | "Friendly" | "Formal" | "Concise" | "Polite" | "Persuasive"
    length: "Short" | "Medium" | "Detailed"
    """
    return f"""You are a professional email editor.

Rewrite the following email/message in a {tone.lower()} tone, at a {length.lower()} length.

Rules:
- Preserve the original meaning and all key facts — do not add information that wasn't there.
- Keep it copy-ready: no placeholder brackets like [Name] unless the original had them.
- Do not include a preamble like "Here is the rewritten email" — output only the rewritten email itself.

Original Email:
\"\"\"
{email_text}
\"\"\"
"""