# prompts/presentation.py

def build_presentation_prompt(topic: str, audience: str, num_slides: int, purpose: str, detail_level: str) -> str:
    """
    Builds the prompt for the Presentation Outline Generator tool.
    detail_level: "Basic" | "Detailed" | "In-depth"
    """
    return f"""You are a presentation design assistant.

Create a slide-by-slide outline for a presentation with these parameters:
- Topic: {topic}
- Audience: {audience}
- Purpose: {purpose}
- Number of slides: {num_slides}
- Detail level: {detail_level}

For EACH slide, output in this exact format:

**Slide N — [Slide Title]**
- Main Points: (2-4 bullet points)
- Suggested Visual: (one short suggestion, e.g. chart, diagram, photo, icon set)
- Speaker Notes: (1-2 sentences, only if detail level is "Detailed" or "In-depth")

Rules:
- Slide 1 must be a title slide, the last slide must be a closing/summary or Q&A slide.
- Keep bullet points concise, not full paragraphs.
- Do not repeat the same content across slides.
"""