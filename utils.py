import streamlit as st
import nltk
import difflib
from nltk.corpus import wordnet
from textblob import TextBlob

# --- Download necessary NLTK data ---
try:
    nltk.data.find('corpora/wordnet')
except LookupError:
    nltk.download('wordnet', quiet=True)

try:
    nltk.data.find('corpora/omw-1.4')
except LookupError:
    nltk.download('omw-1.4', quiet=True)

# --- Page & Style Setup ---
def setup_css():
    st.set_page_config(
        page_title="Linguify AI Toolkit - Enhanced",
        page_icon="📝",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    st.markdown("""<style>
        .stApp {
            background: linear-gradient(135deg, #89f7fe 0%, #66a6ff 100%);
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            color: #0f1b2f;
            padding-bottom: 50px;
        }
        .css-1d391kg { background-color: #112d4e !important; color: white; }
        .css-1d391kg a, .css-1d391kg p { color: white !important; }
        .css-18e3th9 {
            background-color: #f0f4f8 !important;
            padding: 2rem 3rem 3rem 3rem;
            border-radius: 12px;
            box-shadow: 0 8px 24px rgb(0 0 0 / 0.15);
            margin: 1rem;
        }
        button.css-18ni7ap {
            background-color: #3f72af !important;
            color: white !important;
            font-weight: 700 !important;
            border-radius: 12px !important;
            padding: 0.8rem 1.5rem !important;
            font-size: 1.2rem !important;
            transition: background-color 0.3s ease;
            margin: 0.5rem 0.25rem;
        }
        button.css-18ni7ap:hover {
            background-color: #112d4e !important;
            color: #89f7fe !important;
        }
        h1, h2, h3, h4 {
            font-weight: 700 !important;
            color: #112d4e !important;
        }
        .diff_insert { background-color: #d4f7d4; font-weight: bold; }
        .diff_delete { background-color: #f7d4d4; text-decoration: line-through; }
        .diff_replace { background-color: #fff3b0; font-weight: bold; }
        .copy-btn {
            cursor: pointer;
            padding: 0.2rem 0.5rem;
            background-color: #3f72af;
            color: white;
            border-radius: 6px;
            font-size: 0.9rem;
            user-select: none;
            margin-left: 10px;
        }
        .copy-btn:hover {
            background-color: #112d4e;
        }
        .button-group {
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
        }
    </style>""", unsafe_allow_html=True)

# --- JavaScript for clipboard copy ---
copy_js = """
<script>
function copyToClipboard(id) {
  const text = document.getElementById(id).innerText;
  navigator.clipboard.writeText(text);
  alert("Copied to clipboard!");
}
</script>
"""

def inject_copy_js():
    st.markdown(copy_js, unsafe_allow_html=True)

# --- Synonym Finder ---
def get_synonyms(word):
    synonyms = set()
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            candidate = lemma.name().replace("_", " ")
            if " " not in candidate:  # single-word only
                synonyms.add(candidate)
    return list(synonyms)[:5]

# --- Text Difference Highlighter ---
def highlight_diff(original, paraphrased):
    diff = difflib.ndiff(original.split(), paraphrased.split())
    result = []
    for d in diff:
        code = d[0]
        word = d[2:]
        if code == ' ':
            result.append(word)
        elif code == '-':
            result.append(f'<span class="diff_delete">{word}</span>')
        elif code == '+':
            result.append(f'<span class="diff_insert">{word}</span>')
    return " ".join(result)

# --- Grammar Correction ---
def check_grammar(text):
    blob = TextBlob(text)
    return str(blob.correct())

# --- Stub Function for Humanizer ---
def humanize_text_stub(text):
    return text  # Replace with real model response when ready
