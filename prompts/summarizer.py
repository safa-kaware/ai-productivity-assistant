# prompts/summarizer.py

def build_summary_prompt(notes: str, length: str, tone: str) -> str:
    """
    Builds the prompt for the Meeting Summarizer tool.
    length: "Short" | "Medium" | "Detailed"
    tone: "Neutral" | "Formal" | "Casual"
    """
    return f"""You are a professional meeting-notes assistant.
Summarize the following meeting notes in a {length.lower()}, {tone.lower()} style.

Structure your response using these exact section headers:

### Summary
### Key Discussion Points
### Important Decisions
### Action Items
### Deadlines

Rules:
- If a section has no relevant information, write "Not specified" under it.
- Do not invent information that isn't in the notes.
- Keep formatting clean with bullet points where appropriate.

Meeting Notes:
\"\"\"
{notes}
\"\"\"
"""