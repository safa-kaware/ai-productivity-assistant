# prompts/action_items.py

def build_action_items_prompt(text: str) -> str:
    """
    Builds the prompt for the Action Item Generator tool.
    Output must be a markdown table: Task | Responsible Person | Deadline | Priority
    """
    return f"""You are an assistant that extracts action items from meeting or discussion text.

Read the text below and output a markdown table with these exact columns:
| Task | Responsible Person | Deadline | Priority |

Rules:
- If the responsible person, deadline, or priority is not mentioned, write "Not specified" in that cell. Never invent a name, date, or priority.
- Priority should be one of: High, Medium, Low, or "Not specified" if not implied by the text.
- Each row should be one distinct, actionable task.
- If no action items exist at all, output exactly: "No action items found in this text."

Text:
\"\"\"
{text}
\"\"\"
"""