# ⚡ AI Productivity Assistant

> One workspace. Every productivity task. Powered by AI.

A modern, AI-powered productivity dashboard built with Streamlit and the Groq API. Combines 8 real-world productivity tools — meeting summarization, email rewriting, presentation outlining, and more — into a single, cohesive workspace with a custom-designed interface.

## ✨ Features

| Tool | What it does |
|---|---|
| 📝 Meeting Summarizer | Turns raw meeting notes into a structured summary with decisions, action items, and deadlines |
| ✅ Action Item Generator | Extracts tasks into a clean table with owner, deadline, and priority |
| 📧 Email Rewriter | Rewrites emails in a chosen tone and length, copy-ready |
| 📊 Presentation Outline Generator | Builds a full slide-by-slide outline with visuals and speaker notes |
| 💼 LinkedIn Post Generator | Drafts a complete post with hook, body, CTA, and hashtags |
| 💡 Brainstorming Tool | Generates distinct, structured ideas at a chosen creativity level |
| 🌐 Translator | Translates text with an alternative phrasing and language notes |
| 📚 Study Notes Generator | Produces structured, exam-ready notes with keywords and sample questions |

Every tool shares the same output handling — a persistent History log (saved to disk, survives restarts) and one-click download as `.txt`.

## 🖼️ Screenshots

*(Add 2-4 screenshots here — Home dashboard, one tool in use, and the History page work well)*

## 🛠️ Tech Stack

- **Frontend:** Streamlit with a custom CSS design system (no default Streamlit look)
- **AI:** [Groq API](https://groq.com) — `openai/gpt-oss-120b`
- **Language:** Python 3
- **Persistence:** Local JSON file for history (no database — deliberate choice for a single-user app; see *Architecture* below)

## 🏗️ Architecture

- **`prompts/`** — one module per tool, each building a carefully engineered prompt. Prompts are kept separate from UI code so they can be tuned independently.
- **`services/groq_service.py`** — the single point of contact with the Groq API. Every tool calls the same `generate_response()` function, so API logic, error handling, and model selection live in exactly one place.
- **`utils/helpers.py`** — history persistence (JSON file, since a single-user local app doesn't need a database).
- **`app.py`** — UI layer: page routing, layout, and wiring inputs to the right prompt + service call.

This separation means adding a 9th tool later only touches `prompts/` and one block in `app.py` — the service layer never changes.

## 🚀 Installation

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/ai-productivity-assistant.git
cd ai-productivity-assistant

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows

# 3. Install dependencies
pip install -r requirements.txt
```

## 🔑 Environment Variables

Create a `.env` file in the project root (copy from `.env.example`):

```text
GROQ_API_KEY=your_groq_api_key_here
GROQ_MODEL=openai/gpt-oss-120b
```

Get a free API key from [console.groq.com](https://console.groq.com).

> **Note:** `.env` is git-ignored and never committed. Never share your real API key.

## ▶️ Running Locally

```bash
streamlit run app.py
```

The app will open automatically at `http://localhost:8501`.




## 🔮 Future Enhancements

- Audio meeting input via speech-to-text before summarization
- Export to PDF/DOCX in addition to TXT
- User accounts with per-user history (would justify moving to a real database)
- Deployment to Streamlit Community Cloud

## 👤 Author

**Safa**
B.E. Computer Science (AI & ML), Gharda Institute of Technology

---

*Built as a capstone project to demonstrate practical LLM integration, prompt engineering, and clean application architecture.*
