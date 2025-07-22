import streamlit as st
from google.generativeai import GenerativeModel

model = GenerativeModel('models/gemini-2.0-flash')

def humanize_text(text):
    if not text.strip():
        return ""
    prompt = f"Rewrite this text to sound more natural and human-friendly without changing the meaning (Result Only):\n\n{text}"
    response = model.generate_content(prompt)
    return response.text.strip()

def humanizer_ui():
    st.subheader("🤖 Humanize Your Text")
    humanize_input = st.text_area(
        "Enter text to humanize:",
        value=st.session_state.input_text,
        height=200,
        placeholder="Type or paste your text..."
    )
    if not humanize_input.strip():
        st.info("Please enter some text above to get started.")
        st.stop()

    if st.button("🧑‍🎤 Humanize Text"):
        with st.spinner("Generating humanized text..."):
            humanized = humanize_text(humanize_input)
            st.session_state.humanized_text = humanized
            st.session_state.input_text = humanize_input

    if st.session_state.humanized_text:
        st.markdown("### ✨ Humanized Text Output")
        st.markdown(f'<div id="humanized_output" style="font-size:1.1rem; line-height:1.6;">{st.session_state.humanized_text}</div>', unsafe_allow_html=True)
        st.markdown(f'<span class="copy-btn" onclick="copyToClipboard(\'humanized_output\')">📋 Copy Output</span>', unsafe_allow_html=True)
        if st.button("📝 Use Humanized Text as Input"):
            st.session_state.input_text = st.session_state.humanized_text
            st.experimental_rerun()
