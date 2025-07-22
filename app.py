import os
import google.generativeai as genai
from dotenv import load_dotenv

# Configure your Google Gemini API key here
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

import streamlit as st
from utils import setup_css, copy_js
from paraphraser import paraphraser_ui
from grammar_checker import grammar_checker_ui
from synonym_finder import synonym_finder_ui
from tone_analyzer import tone_analyzer_ui
from readability_checker import readability_checker_ui
from humanizer import humanizer_ui

# --- CSS & UI Setup ---
setup_css()
st.markdown(copy_js, unsafe_allow_html=True)

# --- SESSION STATE INIT ---
if "input_text" not in st.session_state:
    st.session_state.input_text = ""
if "paraphrased_text" not in st.session_state:
    st.session_state.paraphrased_text = ""
if "humanized_text" not in st.session_state:
    st.session_state.humanized_text = ""
if "history" not in st.session_state:
    st.session_state.history = []

# --- Sidebar ---
st.sidebar.title("🛠 Linguify Toolkit")
tool = st.sidebar.radio(
    "Choose a Tool",
    [
        "Paraphraser (Start Here)",
        "Grammar Checker",
        "Synonym Finder",
        "Tone Analyzer",
        "Readability Checker",
        "Humanize Text"
    ]
)
st.sidebar.markdown("---")
st.sidebar.markdown("Created with ❤️ by Rhonzkiee. Powered by Google Gemini and Streamlit.")

# --- Title ---
st.title("📝 Linguify AI Toolkit - Enhanced")

# --- Tool Routing ---
if tool == "Paraphraser (Start Here)":
    paraphraser_ui()
elif tool == "Grammar Checker":
    grammar_checker_ui()
elif tool == "Synonym Finder":
    synonym_finder_ui()
elif tool == "Tone Analyzer":
    tone_analyzer_ui()
elif tool == "Readability Checker":
    readability_checker_ui()
elif tool == "Humanize Text":
    humanizer_ui()

# --- Common Text Metrics ---
with st.expander("📊 Text Metrics", expanded=True):
    word_count = len(st.session_state.input_text.split())
    char_count = len(st.session_state.input_text)
    st.metric("Word Count", word_count)
    st.metric("Character Count", char_count)

st.markdown("---")
st.caption("© 2025 Linguify. Powered by Google Gemini & Streamlit.")
