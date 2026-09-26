# app.py
import streamlit as st
from services.groq_service import generate_response
from prompts.summarizer import build_summary_prompt
from prompts.action_items import build_action_items_prompt
from prompts.email import build_email_prompt
from prompts.presentation import build_presentation_prompt
from prompts.linkedin import build_linkedin_prompt
from prompts.brainstorm import build_brainstorm_prompt
from prompts.translator import build_translation_prompt
from prompts.study_notes import build_study_notes_prompt
from utils.helpers import init_history, add_to_history, clear_history

st.set_page_config(
    page_title="AI Productivity Assistant",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

init_history()

# ---------------------------------------------------------------
# GLOBAL CSS — design system (colors, typography, cards, spacing)
# ---------------------------------------------------------------
st.markdown("""
<style>
    :root {
        --bg: #0E1117;
        --surface: #161B22;
        --border: #262C36;
        --text: #E6E8EB;
        --text-dim: #9AA3AF;
        --accent: #4F8DFD;
        --accent2: #8B5CF6;
    }

    .stApp { background-color: var(--bg); color: var(--text); }

    [data-testid="stSidebar"] {
        background-color: var(--surface);
        border-right: 1px solid var(--border);
    }

    h1, h2, h3 { color: var(--text) !important; font-weight: 700 !important; }

    .hero {
        padding: 48px 0 32px 0;
        text-align: center;
    }
    .hero h1 {
        font-size: 2.6rem !important;
        background: linear-gradient(90deg, var(--accent), var(--accent2));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 8px !important;
    }
    .hero p {
        color: var(--text-dim);
        font-size: 1.05rem;
        max-width: 560px;
        margin: 0 auto;
    }

    .tool-card {
        background-color: var(--surface);
        border: 1px solid var(--border);
        border-radius: 12px;
        padding: 20px;
        height: 100%;
        transition: border-color 0.15s ease, transform 0.15s ease;
    }
    .tool-card:hover {
        border-color: var(--accent);
        transform: translateY(-2px);
    }
    .tool-card .icon { font-size: 1.6rem; }
    .tool-card h4 {
        color: var(--text) !important;
        margin: 8px 0 4px 0 !important;
        font-size: 1.05rem !important;
    }
    .tool-card p {
        color: var(--text-dim);
        font-size: 0.88rem;
        margin-bottom: 0;
    }

    div.stButton > button {
        background: linear-gradient(90deg, var(--accent), var(--accent2));
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.5rem 1.2rem;
        font-weight: 600;
    }
    div.stButton > button:hover {
        opacity: 0.9;
    }

    .output-box {
        background-color: var(--surface);
        border: 1px solid var(--border);
        border-radius: 10px;
        padding: 20px;
        margin-top: 16px;
    }

    .sidebar-footer {
        position: fixed;
        bottom: 12px;
        font-size: 0.75rem;
        color: var(--text-dim);
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------------
# SIDEBAR NAVIGATION
# ---------------------------------------------------------------
with st.sidebar:
    st.markdown("## ⚡ AI Productivity Assistant")
    st.markdown("---")

    page = st.radio(
        "Navigate",
        [
            "🏠 Home",
            "📝 Meeting Summarizer",
            "✅ Action Items",
            "📧 Email Rewriter",
            "📊 Presentation Builder",
            "💼 LinkedIn Writer",
            "💡 Brainstorm",
            "🌐 Translator",
            "📚 Study Notes",
            "🕘 History",
            "ℹ️ About",
        ],
        label_visibility="collapsed",
    )

    st.markdown('<div class="sidebar-footer">Built with Streamlit + Groq</div>', unsafe_allow_html=True)

# ---------------------------------------------------------------
# TOOL DEFINITIONS (used to render Home cards)
# ---------------------------------------------------------------
TOOLS = [
    ("📝", "Meeting Summarizer", "Turn long meeting notes into concise, structured summaries."),
    ("✅", "Action Items", "Extract tasks, owners, and deadlines from any discussion."),
    ("📧", "Email Rewriter", "Rewrite emails in the tone and length you need."),
    ("📊", "Presentation Builder", "Generate full slide-by-slide outlines from a topic."),
    ("💼", "LinkedIn Writer", "Draft copy-ready posts with hooks and hashtags."),
    ("💡", "Brainstorm", "Generate structured, non-repetitive ideas on demand."),
    ("🌐", "Translator", "Translate text naturally between languages."),
    ("📚", "Study Notes", "Turn any topic into structured, exam-ready notes."),
]


def download_button(result: str, filename: str):
    """Reusable download button for any tool's output."""
    st.download_button(
        label="⬇ Download as TXT",
        data=result,
        file_name=filename,
        mime="text/plain",
    )


# ---------------------------------------------------------------
# PAGE ROUTING
# ---------------------------------------------------------------
if page == "🏠 Home":
    st.markdown("""
    <div class="hero">
        <h1>AI Productivity Assistant</h1>
        <p>Work smarter. Create faster. Think better. Your intelligent workspace for everyday tasks.</p>
    </div>
    """, unsafe_allow_html=True)

    cols = st.columns(4)
    for i, (icon, name, desc) in enumerate(TOOLS):
        with cols[i % 4]:
            st.markdown(f"""
            <div class="tool-card">
                <div class="icon">{icon}</div>
                <h4>{name}</h4>
                <p>{desc}</p>
            </div>
            """, unsafe_allow_html=True)
            st.write("")

elif page == "📝 Meeting Summarizer":
    st.header("📝 Meeting Summarizer")
    st.caption("Paste your meeting notes and get a structured summary.")

    notes = st.text_area("Meeting Notes", height=220, placeholder="Paste your raw meeting notes here...")

    col1, col2 = st.columns(2)
    with col1:
        length = st.selectbox("Summary Length", ["Short", "Medium", "Detailed"])
    with col2:
        tone = st.selectbox("Tone", ["Neutral", "Formal", "Casual"])

    if st.button("Generate Summary"):
        if not notes.strip():
            st.warning("Please paste some meeting notes first.")
        else:
            with st.spinner("Generating summary..."):
                prompt = build_summary_prompt(notes, length, tone)
                result = generate_response(prompt)
            add_to_history("Meeting Summarizer", "📝", result)
            st.markdown(f'<div class="output-box">{result}</div>', unsafe_allow_html=True)
            download_button(result, "meeting_summary.txt")

elif page == "✅ Action Items":
    st.header("✅ Action Item Generator")
    st.caption("Paste any discussion or meeting text to extract structured tasks.")

    text = st.text_area("Discussion / Notes", height=220, placeholder="Paste your text here...")

    if st.button("Extract Action Items"):
        if not text.strip():
            st.warning("Please paste some text first.")
        else:
            with st.spinner("Extracting action items..."):
                prompt = build_action_items_prompt(text)
                result = generate_response(prompt)
            add_to_history("Action Items", "✅", result)
            st.markdown(result)
            download_button(result, "action_items.txt")

elif page == "📧 Email Rewriter":
    st.header("📧 Email Rewriter")
    st.caption("Paste your email and choose how you want it rewritten.")

    email_text = st.text_area("Your Email / Message", height=200, placeholder="Paste your draft here...")

    col1, col2 = st.columns(2)
    with col1:
        tone = st.selectbox("Tone", ["Professional", "Friendly", "Formal", "Concise", "Polite", "Persuasive"])
    with col2:
        length = st.selectbox("Length", ["Short", "Medium", "Detailed"])

    if st.button("Rewrite Email"):
        if not email_text.strip():
            st.warning("Please paste an email first.")
        else:
            with st.spinner("Rewriting..."):
                prompt = build_email_prompt(email_text, tone, length)
                result = generate_response(prompt)
            add_to_history("Email Rewriter", "📧", result)
            st.markdown(f'<div class="output-box">{result}</div>', unsafe_allow_html=True)
            st.text_area("Copy from here", value=result, height=200)
            download_button(result, "rewritten_email.txt")

elif page == "📊 Presentation Builder":
    st.header("📊 Presentation Outline Generator")
    st.caption("Describe your presentation and get a full slide-by-slide outline.")

    topic = st.text_input("Topic", placeholder="e.g. Introduction to Machine Learning")
    audience = st.text_input("Audience", placeholder="e.g. First-year engineering students")

    col1, col2 = st.columns(2)
    with col1:
        num_slides = st.slider("Number of Slides", min_value=3, max_value=20, value=8)
    with col2:
        detail_level = st.selectbox("Detail Level", ["Basic", "Detailed", "In-depth"])

    purpose = st.text_input("Purpose", placeholder="e.g. Explain core concepts for a lab session")

    if st.button("Generate Outline"):
        if not topic.strip():
            st.warning("Please enter a topic first.")
        else:
            with st.spinner("Building outline..."):
                prompt = build_presentation_prompt(topic, audience or "General audience", num_slides, purpose or "Inform", detail_level)
                result = generate_response(prompt, max_tokens=2048)
            add_to_history("Presentation Builder", "📊", result)
            st.markdown(result)
            download_button(result, "presentation_outline.txt")

elif page == "💼 LinkedIn Writer":
    st.header("💼 LinkedIn Post Generator")
    st.caption("Turn a project, achievement, or idea into a copy-ready LinkedIn post.")

    topic = st.text_input("Topic", placeholder="e.g. Launching my capstone project")
    achievement = st.text_area("Achievement / Project Details", height=120, placeholder="Describe what you did, in your own words...")

    col1, col2, col3 = st.columns(3)
    with col1:
        tone = st.selectbox("Tone", ["Professional", "Casual", "Inspirational", "Bold", "Reflective"])
    with col2:
        audience = st.text_input("Audience", placeholder="e.g. Recruiters, fellow students")
    with col3:
        length = st.selectbox("Length", ["Short", "Medium", "Detailed"])

    if st.button("Generate Post"):
        if not achievement.strip():
            st.warning("Please describe your achievement or project first.")
        else:
            with st.spinner("Writing your post..."):
                prompt = build_linkedin_prompt(topic or "Professional update", achievement, tone, audience or "Professional network", length)
                result = generate_response(prompt)
            add_to_history("LinkedIn Writer", "💼", result)
            st.markdown(f'<div class="output-box">{result}</div>', unsafe_allow_html=True)
            st.text_area("Copy from here", value=result, height=250)
            download_button(result, "linkedin_post.txt")

elif page == "💡 Brainstorm":
    st.header("💡 Brainstorming Tool")
    st.caption("Generate structured, distinct ideas for any problem or topic.")

    topic = st.text_area("Topic / Problem", height=120, placeholder="e.g. Ways to improve student engagement in online classes")

    col1, col2, col3 = st.columns(3)
    with col1:
        num_ideas = st.slider("Number of Ideas", min_value=3, max_value=10, value=5)
    with col2:
        domain = st.text_input("Industry / Domain", placeholder="e.g. Education, Healthcare, Retail")
    with col3:
        creativity = st.selectbox("Creativity Level", ["Practical", "Balanced", "Wild / Unconventional"])

    if st.button("Generate Ideas"):
        if not topic.strip():
            st.warning("Please describe a topic or problem first.")
        else:
            with st.spinner("Brainstorming..."):
                prompt = build_brainstorm_prompt(topic, num_ideas, domain or "General", creativity)
                result = generate_response(prompt, max_tokens=2048)
            add_to_history("Brainstorm", "💡", result)
            st.markdown(result)
            download_button(result, "brainstorm_ideas.txt")

elif page == "🌐 Translator":
    st.header("🌐 Translator")
    st.caption("Translate text between languages, with optional notes.")

    text = st.text_area("Text to Translate", height=150, placeholder="Enter text here...")

    col1, col2 = st.columns(2)
    with col1:
        source_lang = st.text_input("Source Language", value="English")
    with col2:
        target_lang = st.text_input("Target Language", placeholder="e.g. Marathi, Hindi, Spanish")

    if st.button("Translate"):
        if not text.strip():
            st.warning("Please enter some text first.")
        elif not target_lang.strip():
            st.warning("Please specify a target language.")
        else:
            with st.spinner("Translating..."):
                prompt = build_translation_prompt(text, source_lang or "auto-detected language", target_lang)
                result = generate_response(prompt)
            add_to_history("Translator", "🌐", result)
            st.markdown(f'<div class="output-box">{result}</div>', unsafe_allow_html=True)
            download_button(result, "translation.txt")

elif page == "📚 Study Notes":
    st.header("📚 Study Notes Generator")
    st.caption("Turn any topic or text into structured, exam-ready notes.")

    topic = st.text_area("Topic or Text", height=180, placeholder="e.g. Explain Normalization in DBMS, or paste a textbook paragraph...")

    col1, col2, col3 = st.columns(3)
    with col1:
        academic_level = st.selectbox("Academic Level", ["School", "Undergraduate", "Postgraduate"])
    with col2:
        note_style = st.selectbox("Note Style", ["Concise", "Detailed", "Exam-Focused"])
    with col3:
        length = st.selectbox("Length", ["Short", "Medium", "Long"])

    if st.button("Generate Notes"):
        if not topic.strip():
            st.warning("Please enter a topic or text first.")
        else:
            with st.spinner("Generating notes..."):
                prompt = build_study_notes_prompt(topic, academic_level, note_style, length)
                result = generate_response(prompt, max_tokens=2048)
            add_to_history("Study Notes", "📚", result)
            st.markdown(result)
            download_button(result, "study_notes.txt")

elif page == "🕘 History":
    st.header("🕘 Recent Activity")

    if not st.session_state.history:
        st.info("No activity yet. Try one of the AI tools to see it appear here.")
    else:
        if st.button("🗑️ Clear History"):
            clear_history()
            st.rerun()
        for entry in st.session_state.history:
            with st.expander(f"{entry['icon']} {entry['tool']} — {entry['timestamp']}"):
                st.markdown(entry['result'])

elif page == "ℹ️ About":
    st.header("ℹ️ About")
    st.write("Built as a capstone project using Streamlit and the Groq API.")
    st.markdown("""
    **Tech stack:** Python, Streamlit, Groq API (`openai/gpt-oss-120b`)

    **Architecture:** UI → Prompt Builder → Groq Service → Groq LLM → Formatted Output

    A single workspace combining 8 AI-powered productivity tools for meeting notes, emails, presentations, social content, brainstorming, translation, and study notes.
    """)