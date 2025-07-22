
## Linguify AI Toolkit
====================

🔗 Live Demo: https://linguifyy.streamlit.app/

## Overview
--------
Linguify is an AI-powered writing enhancement web app designed to help students, professionals, and content creators improve their writing in real-time using multiple language tools. Built using Streamlit and powered by Google Gemini AI, Linguify allows users to paraphrase, check grammar, find synonyms, analyze tone, measure readability, and humanize text all in one seamless interface.

## 🎯 Problem It Solves
--------------------
Many individuals, especially students and professionals, struggle with:
- Repetitive or robotic writing.
- Grammatical errors.
- Inappropriate tone for context.
- Difficult-to-read sentences.
- Lack of vocabulary diversity.

Linguify addresses these problems by providing a toolkit of language tools to refine and enhance content with ease.

## 👥 Target Demographic
----------------------
- **Students**: For refining essays, reports, and thesis work.
- **Professionals**: For emails, proposals, and presentations.
- **Writers & Bloggers**: For crafting high-quality content faster.
- **ESL Learners**: For improving English writing fluency.

## 🛠 Features
-----------
✅ Paraphraser (Start Here)  
✅ Grammar Checker  
✅ Synonym Finder  
✅ Tone Analyzer  
✅ Readability Checker  
✅ Humanizer (Make text sound more natural)

## 🧠 Powered By
-------------
- Google Gemini API (via `google.generativeai`)
- Streamlit for UI
- NLP libraries: `nltk`, `textstat`, etc.

## 📂 File Structure
-----------------
```
- `app.py`: Main entry point of the app.
- `utils.py`: UI styles and helpers.
- `paraphraser.py`: Paraphrasing logic and UI.
- `grammar_checker.py`: Grammar correction functionality.
- `synonym_finder.py`: Synonym extraction using WordNet.
- `tone_analyzer.py`: Detects tone (formal, casual, etc.).
- `readability_checker.py`: Computes readability scores.
- `humanizer.py`: Converts robotic text into human-like writing.
```
## 🧪 Installation
---------------
1. Clone the repository:
   git clone https://github.com/darknecrocities/Linguify.git

2. Navigate into the project folder:
   cd Linguify

3. Install dependencies:
   pip install -r requirements.txt

4. Create a `.env` file and add your Gemini API key:
   GEMINI_API_KEY=your_google_api_key_here

5. Run the app:
   streamlit run app.py

## 📌 Notes
--------
- Make sure `nltk` corpora like `wordnet` are downloaded using:
  ```python
  import nltk
  nltk.download('wordnet')
  ```

## 💡 Future Plans
---------------
- Support for multilingual paraphrasing
- Export to PDF/Word
- Integration with Google Docs or Notion
- User login and personalized history

## 📢 Feedback or Contributions?
-----------------------------
Feel free to fork the repo, suggest improvements, or report issues via GitHub!


© 2025 Linguify – Made with ❤️ using Streamlit and Gemini AI Created by: Arron Parejas
