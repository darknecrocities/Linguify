import streamlit as st
import textstat

def readability_score(text):
    try:
        score = textstat.flesch_reading_ease(text)
    except:
        score = 0
    return score

def complexity_level(text):
    try:
        level = textstat.text_standard(text, float_output=False)
    except:
        level = "Unknown"
    return level

def readability_checker_ui():
    input_text = st.text_area(
        "Enter your text here:",
        value=st.session_state.input_text,
        height=200,
        placeholder="Type or paste your text..."
    )
    st.session_state.input_text = input_text
    st.subheader("📚 Readability & Complexity")
    score = readability_score(input_text)
    level = complexity_level(input_text)
    st.write(f"**Flesch Reading Ease Score:** {score:.2f}")
    st.write(f"**Estimated Grade Level:** {level}")
