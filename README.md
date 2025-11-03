# 🚀 AI Profile & Resume Analyzer

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.33-red?style=for-the-badge&logo=streamlit)
![SpaCy](https://img.shields.io/badge/spaCy-3.7-brightgreen?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNTAgMjUwIj48cGF0aCBmaWxsPSIjMDBhNmYwIiBkPSJNMjQ5LjYgMTQzLjJjLTEuOC00LjYtMy45LTkuMS02LjQtMTMuM2EzLjIgMy4yIDAgMCAwLTMuMi0xLjcgMS40IDEuNCAwIDAgMC0xLjMgMS4yYy0xLjMgMy4yLTIuMyA2LjYtMy4xIDEwYTEwLjIgMTAuMiAwIDAgMS0zLjUgNy4yYy0uMi01LjEtLjEtMTAuMi0uMi0xNS4zIDAtMi44LS4xLTUuNy0uMy04LjUgMC0uMS0uMS0uMy0uMS0uNGwtMi4yLTI4LjIgMy41LTMxLjgtNi4yLTI2LjktNC4yIDIyLjMtMi43LTIuMi0zLjUgMi4yIDMuNyAzLjQtMi40IDIzLjYtMi4xIDIxLjcgMCAuMi4xLjQuMS43di4zYzAgMy45LjQgNy44LjEgMTEuN2EyLjggMi44IDAgMCAxLTIuNyAyLjVjLTE1My42IDAtMTUzLjYgMC0xNTMuNiAwIEw0LjMgMTQyLjUgMyA5Ni44bDI4LjMtMTMuMyAzLjQgNy4xIDEyLjMgNDkuOSAyOC40IDEyLjctMi4yIDE1LjcgMTQuNSAxNC41IDE1LjktMi4xIDI4LjEgMTIuNi0yOC4xIDkuOSAxNS45IDE4LjEgNi45IDkuOS05LjkgMTAuNiAxMi45IDEwLjYtOS45IDExLjcgMTYuMiAxMy40IDYuMy0xMy4zIDI5LjgtMTMuMiA5LjMgNy4xIDE3LjYtOS4xIDE3LjQtNy4xIDEwLjEgMjYuOS0xNi41IDIyLjYtMTcgOC4xIDYuNyAyOC42LTEzLjEtMTIuOSAxMy4xIDEyLjkgMTMuMS0xMy4xIDEyLjkgMTMuMSAyMC4yLTMzLjcgMTEuNyAxMC42IDI4LjgtMjEuMiAyOC44IDIxLjItMjMuNCAxMC42LTExLjktMTEuNyA0LjQtMTAuNi00LjQtMTAuNiA0LjQtMTAuNi00LjQgMTAuNiA0LjQtMTAuNi0yLjQtMjMuNSAyLjQgMTAuNi0yLjQtMTAuNi0xMC42LTIuNCAxMC42LTIuNC0yMS4xLTEwLjYgMjEuMUwxNDMuNiAzNWwxMy4xLTIxLjIgMTEuMSAxMC42TDYwLjIgMTAyLjIgNTMuMyA2MGwzLjQgMi4yLTIuMi0xMy4xLTI144LTEyLjQgNy40IDQyLjYgMi4yIDM2LjggMTEuNyA1LjIgNy44LTEwLjYtNy44LTEwLjcgMTEuMS0xMC42TDcxLjQgOTMuOWwxMS45LTEyLjQgMy45IDE2LjcgMTAuNC03LjcgMy45IDIzLjQgMTIuMS0xMC42IDEyLjEgMjEuMi0zLjEgNy44IDE4LjEgMTMuMS0yMy40IDEyLjYgMTAuNi0xNS45IDEyLjYgMTUuOSA4LjgtMjMuNCA4LjQgMjMuNCA4LjgtMjMuNCA4LjQgMjMuNC04LjQgMjMuNGExMi42IDEyLjYgMCAwIDEtNC45IDEwLjIgMTMuNyAxMy43IDAgMCAxLTEzIDEuMmMtMTYuNy0xLjktMjQuNiAxMy42LTI0LjYgMTMuNi0uMi4zLS41LjUtLjcuNmEyMS44IDIxLjggMCAwIDEtMTYuMiA4LjUgMjMuMyAyMy4zIDAgMCAxLTIxLjMtMTJjLTYuOS0xMC43LTYuOS0yMy45LTYuOS0yMy45cy04LjEtMTUuNy0yMi45LTE1J2MtMTQuNSAwLTIxLjkgMTIuNi0yMS45IDEyLjZzLTYgMTEuMS01LjggMjMuNWMxLjQgOC43IDMuMyAxOC41IDUuOCAyNy4zIDEuMyA0LjIgNC4xIDEzLjMgMTEuNyAxMy4zaDEyLjljNy41IDAgMTAuNC05LjEgMTEuNy0xMy4zIDIuNS04LjggNC40LTE4LjYgNS44LTI3LjMgMS40LTguNy0xLjItMjMuNS0xLjItMjMuNXMxLjktMTIuNi0xMC4yLTEyLjZjLTEyLjMgMC0xMy4zIDEyLjYtMTMuMyAxMi4zIDAgNy4yIDEuOCAxNC4zIDUgMjEuMWEyMy4zIDIzLjMgMCAwIDEgMi44IDQuNCAyLjcgMi43IDAgMCAxIDEgMS44bDEuNS43YzAgLjMgMCAuNS0uMS44bC0uMS42YS44LjggMCAwIDEtLjUuNmwtLTYuNC0uMmEuMy4zIDAgMCAxLS4yIDBsLTEuOS4yYTEgMSAwIDAgMS0uNy0uNC41LjUgMCAwIDEtLjEtLjJsLTUuMS05YTE5LjUgMTkuNSAwIDAgMC00LjYtNi45Yy0zLjYtNC4xLTEwLjYtNi45LTE4LjQtNi45LTE0LjcgMC0yMy40IDEyLjctMjMuNCAxMi43UzM2LjMgNzkuMiAzNi4xIDkxLjdjMCA4LjQgMi45IDE2LjYgOC41IDIyLjEgNC44IDQuOCA5LjMgNi45IDE1IDEuOWwxLjktMy4zIDEuMy0uNy44LS4yLS4yLS41LS4zLS43LS4yLS42LS4yLS41LS4zLS42LS4zLS40YTEzLjYgMTMuNiAwIDAgMC0yLjEtMS40IDE2LjkgMTYuOSAwIDAgMC00LjgtMy4zIDIxLjUgMjEuNSAwIDAgMC0xMy41IDMuMmMtNC42IDQuMS00LjggNC4zLTQuOCA0LjNhMTAzLjIgMTAzLjIgMCAwIDEgMjUuMiAxNGMuMy4xLjEuNC0uMS42bC01LjMgNC45Yy0uMy4zLS41LjItLjYuMWwtOC4yLTMuOGMtLjItLjEtLjQtLjEtLjUuMWwtMTguMyA5LjFhMi4yIDIuMiAwIDAgMC0xLjMgMi44YzIuMyAxMi42IDEyLjkgMjEuMSAyNS4xIDIwLjMgMTQuNy0xIDE1Mi45LS4xIDE1Mi45LS4xIDEwLjEgMCAxNy42LTcuOCAxNy42LTguNiAwLTcuNy00LjYtMTQuMi04LjYtMTguNi01LjgtNS43LTEyLjgtOC42LTE5LjktOC42cy0xNC4yIDMuMS0xOS45IDguN2MtNC4xIDQuMy04LjYgMTAtOC42IDE4LjYgMCAuOCAxNy42IDguNiAxNy42IDguNiAxMi4zLS44IDIyLjgtOS4zIDI1IDEuMiAwIDAgMCAuMS40LjRsMi4zIDE5LjItMi4yIDE3LjYtMS4xIDIuMiAyLjEtMi4xLTMuMiAxNC43LTIuMi0xNC43LTExLjctMTUuNyAxMS43LTE1LjctMTUuNyAxMS43LTE1LjctMTUuNy0xMi45IDIzLjQtMjEuMi0yMy40IDE3LjEtMTQuOC0yMi45IDEzLjEgMjAuMi0yMi44LTEwLjItMTMuMS0xOC40IDEyLjkgMTMuMSAxMC42LTEyLjkgMTMuMVoiLz48L3N2Zz4=)

> An intelligent application built with Python and SpaCy to analyze professional profiles and resumes, providing scorable feedback and targeted advice for job seekers.

This project uses NLP to score a LinkedIn profile and match a resume against a job description, identifying missing keywords and key entities.

---


## 💡 Key Features

This application is divided into two core modules:

| Analyzer | Feature | What It Does |
| :--- | :--- | :--- |
| **LinkedIn** | Profile Score | Provides a score (0-100) based on your "About" and "Skills" sections. |
| | Action Verb Analysis | Checks your "About" section for a high number of impact words (e.g., "managed", "developed"). |
| | Skills Count | Scores you based on the *quantity* of skills you've listed. |
| **Resume** | General Score | Provides a score (0-100) for your resume based on length, action verbs, and section completion. |
| | **Job Match Score** | **(Core AI Feature)** Matches your resume against a job description and provides a % match score. |
| | **Missing Keywords** | Automatically extracts keywords from the job description and shows you exactly which ones are missing from your resume. |
| | **Entity Scanner (NER)** | Uses a Named Entity Recognition model to scan your resume and extract important entities like companies, schools, and locations. |

---

## 🛠️ Technology Stack

This project was built using the following technologies:

* **Python:** The core programming language.
* **Streamlit:** Used to create the interactive web UI.
* **SpaCy:** The core AI/NLP library used for:
    * Named Entity Recognition (NER)
    * Keyword Extraction (Tokenization, Lemmatization)
    * Job Description Matching
* **Plotly:** Used to create the dynamic score charts.
* **PyPDF2:** Used to read and extract text from uploaded PDF resumes.

---

## 🚀 Get it Running

You can get this project running on your local machine in just a few steps.

1.  **Clone the Repository** 📂
    
    Open your terminal and clone the project code to your computer:
    ```bash
    git clone [https://github.com/ArifaTabasum10/AI-Profile-Analyzer.git](https://github.com/ArifaTabasum10/AI-Profile-Analyzer.git)
    cd AI-Profile-Analyzer
    ```

2.  **Install the Libraries** 📦
    
    This project uses a few Python libraries. Install them all at once with this command:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Download the AI Model** 🧠
    
    The app's NLP features run on a SpaCy model. Download the small English model:
    ```bash
    python -m spacy download en_core_web_sm
    ```

4.  **Launch the App!** 🎈
    
    You're all set. Run this command to launch the Streamlit app:
    ```bash
    streamlit run app.py
    ```
    Your web browser will open automatically, and you can start analyzing!

---
## 📸 Screenshots

Here is a preview of the analyzer in action.

<img width="1911" height="900" alt="Screenshot 2025-11-03 205522" src="https://github.com/user-attachments/assets/b278e349-3188-4995-bbdc-84ffe7353cbb" />

