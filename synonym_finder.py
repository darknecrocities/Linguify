import streamlit as st
import re
from utils import get_synonyms

def synonym_finder_ui():
    input_text = st.text_area(
        "Enter your text here:",
        value=st.session_state.input_text,
        height=200,
        placeholder="Type or paste your text..."
    )
    st.session_state.input_text = input_text
    st.subheader("🔤 Synonym Suggestions")
    words = set(re.findall(r'\w+', input_text))
    if not words:
        st.info("No words detected in input.")
        return
    word_choice = st.selectbox("Pick a word to see synonyms", options=sorted(words))
    synonyms = get_synonyms(word_choice)
    if synonyms:
        st.write(f"Synonyms for **{word_choice}**:")
        for syn in synonyms:
            st.write(f"- {syn}")
    else:
        st.info("No synonyms found.")
