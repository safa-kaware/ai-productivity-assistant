# prompts/study_notes.py

def build_study_notes_prompt(topic: str, academic_level: str, note_style: str, length: str) -> str:
    """
    Builds the prompt for the Study Notes Generator tool.
    academic_level: "School" | "Undergraduate" | "Postgraduate"
    note_style: "Concise" | "Detailed" | "Exam-Focused"
    length: "Short" | "Medium" | "Long"
    """
    return f"""You are an academic study notes assistant writing for a {academic_level} level student.

Create {length.lower()}, {note_style.lower()} study notes on the following topic/text.

Structure your response using these exact section headers:

### Definition
### Key Concepts
### Important Points
### Examples
### Advantages / Disadvantages
### Keywords
### Exam Questions
### Quick Revision

Rules:
- If a section genuinely doesn't apply to this topic (e.g. "Advantages / Disadvantages" for a purely definitional topic), write "Not applicable" rather than forcing content.
- Use bullet points, not long paragraphs.
- "Exam Questions" should list 3-5 likely questions a student could be asked.
- "Quick Revision" should be a short, dense recap — a few lines max.

Topic/Text:
\"\"\"
{topic}
\"\"\"
"""