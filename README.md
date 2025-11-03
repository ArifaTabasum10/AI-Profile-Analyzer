# AI-Profile-Analyzer
A Streamlit app that analyzes LinkedIn profiles and resumes using AI/NLP.
🚀 AI Profile & Resume Analyzer
This is an intelligent, locally-run application built with Streamlit and SpaCy that analyzes your professional presence. It provides a "LinkedIn Analyzer" to score your profile summary and a "Resume Analyzer" to score your resume and match it against a job description.

Features
This app is built with a 100% free, offline AI/NLP engine.

LinkedIn Analyzer:

Profile Scoring: Get a score out of 100 for your LinkedIn "About" section and "Skills" list.

Action Verb Analysis: Scans your summary for a sufficient number of high-impact action verbs (e.g., "developed," "managed," "achieved").

Skills Count: Rewards you for listing a comprehensive number of skills.

Data Visualization: See your score at a glance with a dynamic Plotly pie chart.


Resume Analyzer:

General Resume Score: Get a score based on length, action verb usage, and the presence of key sections (like "Education" and "Experience").

Job Match Score: Paste in a job description, and the app will use NLP to extract key skills and tell you your "match percentage."

Missing Keywords: Instantly see a list of important keywords from the job description that are missing from your resume.

Named Entity Recognition (NER): The app automatically scans your resume and extracts key entities like:Companies / Organizations & skills


🛠️ Tech Stack

Language: Python

Framework: Streamlit (for the web UI)

AI/NLP: SpaCy (for NER, keyword extraction, and analysis)

Data Visualization: Plotly (for score charts)

PDF Reading: PyPDF2

🚀 How to Run This Project Locally
Follow these steps to get the application running on your machine.

1. Clone the Repository
Open your terminal and clone this project:
--- git clone https://github.com/ArifaTabasum10/AI-Profile-Analyzer.git
cd AI-Profile-Analyzer
2. Install Dependencies
Install all the required Python libraries using the requirements.txt file:
--- pip install -r requirements.txt
3. Install Dependencies
Install all the required Python libraries using the requirements.txt file:
--- pip install -r requirements.txt
4. Download the SpaCy Model
You'll need the small English model for SpaCy.
--- python -m spacy download en_core_web_sm
5. Run the App
Launch the Streamlit app:
--- streamlit run app.py
The app will automatically open in your web browser.
