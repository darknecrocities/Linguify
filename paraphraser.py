import streamlit as st
import difflib
from utils import get_synonyms
from google.generativeai import GenerativeModel

model = GenerativeModel('models/gemini-2.0-flash')

def paraphrase_with_gemini(text):
    if not text.strip():
        return ""
    prompt = f"Paraphrase fluently and clearly (Result Only):\n\n{text}"
    response = model.generate_content(prompt)
    return response.text.strip()

def synonym_replace_paraphrase(text):
    words = text.split()
    paraphrased_words = []
    for w in words:
        syns = get_synonyms(w)
        if syns:
            replacement = syns[0] if syns[0].lower() != w.lower() else (syns[1] if len(syns) > 1 else w)
            paraphrased_words.append(replacement)
        else:
            paraphrased_words.append(w)
    return " ".join(paraphrased_words)

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
def paraphraser_ui():
    st.markdown("### Enter your text to paraphrase")
    
    # INPUT TEXT AREA — here’s where user types/pastes text
    input_text = st.text_area(
        "Input Text:",
        value=st.session_state.input_text,
        height=200,
        placeholder="Type or paste your text here..."
    )
    
    # Update session state with current input text
    st.session_state.input_text = input_text

    st.markdown("### Choose Paraphrasing Method")
    method = st.radio(
        "Paraphrasing Method:",
        ("Google Gemini (Advanced)", "Local Synonym Replacement (Fast)")
    )

    paraphrase_fn = paraphrase_with_gemini if method == "Google Gemini (Advanced)" else synonym_replace_paraphrase

    col1, col2, col3 = st.columns([1,1,1])
    with col1:
        if st.button("🚀 Apply Paraphrase"):
            with st.spinner("Generating paraphrased text..."):
                paraphrased = paraphrase_fn(input_text)
                st.session_state.paraphrased_text = paraphrased
                st.session_state.history.append({
                    "original": input_text,
                    "paraphrased": paraphrased
                })

    with col2:
        if st.button("🧹 Clear Text"):
            st.session_state.input_text = ""
            st.session_state.paraphrased_text = ""
            if hasattr(st, "experimental_rerun"):
                st.experimental_rerun()

    with col3:
        if st.session_state.paraphrased_text:
            if st.button("📝 Use Paraphrased Text as Input"):
                st.session_state.input_text = st.session_state.paraphrased_text
                if hasattr(st, "experimental_rerun"):
                    st.experimental_rerun()

    if st.session_state.paraphrased_text:
        st.subheader("🔄 Paraphrased Output with Highlights")
        highlighted = highlight_diff(st.session_state.input_text, st.session_state.paraphrased_text)
        st.markdown(f'<div id="paraphrased_output" style="font-size:1.1rem; line-height:1.6;">{highlighted}</div>', unsafe_allow_html=True)
        st.markdown(f'<span class="copy-btn" onclick="copyToClipboard(\'paraphrased_output\')">📋 Copy Output</span>', unsafe_allow_html=True)

    if st.session_state.history:
        with st.expander("🕘 Paraphrase History (click to expand)", expanded=False):
            for i, record in enumerate(reversed(st.session_state.history[-10:]), 1):
                st.markdown(f"**#{i} Original:** {record['original']}")
                st.markdown(f"**Paraphrased:** {record['paraphrased']}")
                st.markdown("---")

def paraphraser_ui():
    st.markdown("### Choose Paraphrasing Method")
    method = st.radio(
        "Paraphrasing Method:",
        ("Google Gemini (Advanced)", "Local Synonym Replacement (Fast)")
    )
    input_text = st.text_area(
        "Enter your text here:",
        value=st.session_state.input_text,
        height=200,
        placeholder="Type or paste your text..."
    )
    st.session_state.input_text = input_text

    paraphrase_fn = paraphrase_with_gemini if method == "Google Gemini (Advanced)" else synonym_replace_paraphrase

    col1, col2, col3 = st.columns([1,1,1])
    with col1:
        if st.button("🚀 Apply Paraphrase"):
            with st.spinner("Generating paraphrased text..."):
                paraphrased = paraphrase_fn(input_text)
                st.session_state.paraphrased_text = paraphrased
                st.session_state.history.append({
                    "original": input_text,
                    "paraphrased": paraphrased
                })

    with col2:
        if st.button("🧹 Clear Text"):
            st.session_state.input_text = ""
            st.session_state.paraphrased_text = ""
            if hasattr(st, "experimental_rerun"):
                st.experimental_rerun()
            else:
                pass  # or handle rerun differently


    with col3:
        if st.session_state.paraphrased_text:
            if st.button("📝 Use Paraphrased Text as Input"):
                st.session_state.input_text = st.session_state.paraphrased_text
                if hasattr(st, "experimental_rerun"):
                    st.experimental_rerun()
                else:
                    pass  # or handle rerun differently


    if st.session_state.paraphrased_text:
        st.subheader("🔄 Paraphrased Output with Highlights")
        highlighted = highlight_diff(st.session_state.input_text, st.session_state.paraphrased_text)
        st.markdown(f'<div id="paraphrased_output" style="font-size:1.1rem; line-height:1.6;">{highlighted}</div>', unsafe_allow_html=True)
        st.markdown(f'<span class="copy-btn" onclick="copyToClipboard(\'paraphrased_output\')">📋 Copy Output</span>', unsafe_allow_html=True)

    if st.session_state.history:
        with st.expander("🕘 Paraphrase History (click to expand)", expanded=False):
            for i, record in enumerate(reversed(st.session_state.history[-10:]), 1):
                st.markdown(f"**#{i} Original:** {record['original']}")
                st.markdown(f"**Paraphrased:** {record['paraphrased']}")
                st.markdown("---")
