# prompts/linkedin.py

def build_linkedin_prompt(topic: str, achievement: str, tone: str, audience: str, length: str) -> str:
    """
    Builds the prompt for the LinkedIn Post Generator tool.
    tone: "Professional" | "Casual" | "Inspirational" | "Bold" | "Reflective"
    length: "Short" | "Medium" | "Detailed"
    """
    return f"""You are a LinkedIn content writer.

Write a LinkedIn post about the following:
- Topic: {topic}
- Achievement/Project details: {achievement}
- Tone: {tone}
- Target audience: {audience}
- Length: {length}

Structure the output using these exact section headers:

### Hook
(A strong 1-2 line opener that stops the scroll)

### Post
(The main body — {length.lower()} length, written in {tone.lower()} tone)

### Call To Action
(Optional — a short line inviting comments, connection, or a link click. If not appropriate, write "Not applicable")

### Hashtags
(3-6 relevant hashtags, space separated)

Rules:
- Do not fabricate specific numbers, company names, or credentials not provided in the input.
- Keep it copy-ready — no placeholder brackets like [Your Name].
"""