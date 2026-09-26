# services/groq_service.py
import os
import streamlit as st
from dotenv import load_dotenv
from groq import Groq, APIError, APIConnectionError, RateLimitError

load_dotenv()


def _get_secret(key: str, default: str = None):
    value = os.getenv(key)
    if value:
        return value
    try:
        return st.secrets[key]
    except Exception:
        return default


API_KEY = _get_secret("GROQ_API_KEY")
DEFAULT_MODEL = _get_secret("GROQ_MODEL", "openai/gpt-oss-120b")

_client = None


def get_client():
    global _client
    if not API_KEY:
        raise ValueError("GROQ_API_KEY is missing. Check your .env file or Streamlit Cloud secrets.")
    if _client is None:
        _client = Groq(api_key=API_KEY)
    return _client


def generate_response(prompt: str, model: str = None, temperature: float = 0.7, max_tokens: int = 1024) -> str:
    if not prompt or not prompt.strip():
        return "⚠️ Please enter some input before generating."

    try:
        client = get_client()
        response = client.chat.completions.create(
            model=model or DEFAULT_MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
            max_tokens=max_tokens,
        )
        return response.choices[0].message.content

    except RateLimitError:
        return "⚠️ Rate limit reached. Please wait a moment and try again."
    except APIConnectionError:
        return "⚠️ Couldn't connect to Groq. Check your internet connection."
    except APIError as e:
        return f"⚠️ Something went wrong while generating your response. ({e.status_code})"
    except Exception as e:
        # TEMPORARY — shows the real error for debugging. Revert once fixed.
        return f"⚠️ DEBUG ERROR: {type(e).__name__}: {str(e)}"