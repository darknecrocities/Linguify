import streamlit as st
from textblob import TextBlob

def analyze_tone(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0.3:
        return "Positive 😊"
    elif polarity < -0.3:
        return "Negative 😠"
    else:
        return "Neutral 😐"

def tone_analyzer_ui():
    input_text = st.text_area(
        "Enter your text here:",
        value=st.session_state.input_text,
        height=200,
        placeholder="Type or paste your text..."
    )
    st.session_state.input_text = input_text
    st.subheader("🎭 Tone Analysis")
    tone = analyze_tone(input_text)
    st.write(f"Detected tone: **{tone}**")
