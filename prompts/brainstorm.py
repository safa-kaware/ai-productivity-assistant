# prompts/brainstorm.py

def build_brainstorm_prompt(topic: str, num_ideas: int, domain: str, creativity: str) -> str:
    """
    Builds the prompt for the Brainstorming Tool.
    creativity: "Practical" | "Balanced" | "Wild / Unconventional"
    """
    return f"""You are a creative brainstorming assistant for the {domain} domain.

Generate exactly {num_ideas} distinct ideas for the following topic/problem, at a "{creativity}" creativity level.

Topic/Problem: {topic}

For EACH idea, output in this exact format:

**Idea N — [Idea Name]**
- Description: (2-3 sentences)
- Why It Matters: (1-2 sentences on the value/impact)
- Potential Implementation: (a short practical note on how to start)
- Difficulty: (Low / Medium / High)

Rules:
- Every idea must be meaningfully different from the others — no rephrasing the same idea twice.
- Match the creativity level: "Practical" = realistic and achievable, "Wild / Unconventional" = bold and less conventional.
"""