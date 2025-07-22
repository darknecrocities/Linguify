import streamlit as st
from textblob import TextBlob

def check_grammar(text):
    blob = TextBlob(text)
    correction = str(blob.correct())
    return correction

def grammar_checker_ui():
    input_text = st.text_area(
        "Enter your text here:",
        value=st.session_state.input_text,
        height=200,
        placeholder="Type or paste your text..."
    )
    st.session_state.input_text = input_text
    st.subheader("🔍 Grammar Check")
    correction = check_grammar(input_text)
    if correction.lower() != input_text.lower():
        st.warning(f"Suggested Correction:\n\n{correction}")
    else:
        st.success("No grammar mistakes found!")
