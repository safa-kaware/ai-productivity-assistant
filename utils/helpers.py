# utils/helpers.py
import streamlit as st
import json
import os
from datetime import datetime

HISTORY_FILE = "history.json"
MAX_ENTRIES = 50


def _load_history_from_disk():
    """Read history from the JSON file. Returns an empty list if the file doesn't exist or is corrupted."""
    if not os.path.exists(HISTORY_FILE):
        return []
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        # File is missing, empty, or corrupted — start fresh rather than crashing the app
        return []


def _save_history_to_disk(history):
    """Write the current history list to the JSON file."""
    try:
        with open(HISTORY_FILE, "w", encoding="utf-8") as f:
            json.dump(history, f, ensure_ascii=False, indent=2)
    except OSError:
        # If disk write fails, fail silently in the UI rather than crashing —
        # history just won't persist for that run.
        pass


def init_history():
    """
    Load history into session_state once per session, from disk if it exists.
    This is what makes history survive an app restart: on first load of a
    session, we read history.json instead of starting from an empty list.
    """
    if "history" not in st.session_state:
        st.session_state.history = _load_history_from_disk()


def add_to_history(tool_name: str, icon: str, result: str):
    """
    Log a generated result to history, both in session_state (for instant UI
    update) and on disk (for persistence across restarts).
    """
    init_history()
    st.session_state.history.insert(0, {
        "tool": tool_name,
        "icon": icon,
        "timestamp": datetime.now().strftime("%I:%M %p, %d %b %Y"),
        "result": result,
    })
    st.session_state.history = st.session_state.history[:MAX_ENTRIES]
    _save_history_to_disk(st.session_state.history)


def clear_history():
    """Clear history from both session_state and disk."""
    st.session_state.history = []
    _save_history_to_disk([])