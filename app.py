import streamlit as st
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from spacy.matcher import Matcher
import PyPDF2
import plotly.graph_objects as go
import re

# --- Streamlit Caching ---
@st.cache_resource
def load_spacy_model():
    """Load and cache the SpaCy model."""
    try:
        return spacy.load("en_core_web_sm")
    except OSError:
        print("Downloading SpaCy model 'en_core_web_sm'...")
        spacy.cli.download("en_core_web_sm")
        return spacy.load("en_core_web_sm")

nlp = load_spacy_model()

# --- Page Configuration ---
st.set_page_config(page_title='AI Profile & Resume Analyzer', page_icon='🚀', layout='wide')

# --- Widen Sidebar CSS ---
st.markdown(
    """
    <style>
    [data-testid="stSidebar"] {
        width: 375px !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title('🚀 100% Free AI Profile & Resume Analyzer')

# --- Helper Functions ---

def extract_text_from_pdf(file):
    text = ''
    try:
        pdf_reader = PyPDF2.PdfReader(file)
        for page in pdf_reader.pages:
            text += page.extract_text()
    except Exception as e:
        st.error(f"Error extracting text from PDF: {e}")
    return text

# --- Keyword Lists ---

POWER_WORDS = [
    'develop', 'build', 'deploy', 'developed', 'managed', 'led', 'achieved', 
    'optimized', 'created', 'launched', 'improved', 'increased', 'negotiated',
    'implemented', 'automated', 'designed', 'built', 'authored', 'mentored', 
    'streamlined', 'trained', 'presented', 'resolved', 'manage', 'lead', 
    'achieve', 'optimize', 'create', 'launch', 'implement', 'automate', 
    'design', 'author', 'mentor', 'train', 'present', 'resolve', 'analyze', 
    'spearhead', 'direct'
]

# NEW: List of tech jargon to prevent NER confusion
TECH_JARGON = {
    'python', 'java', 'sql', 'c++', 'c#', 'javascript', 'react', 'reactjs', 'angular',
    'vue', 'node.js', 'nodejs', 'php', 'swift', 'kotlin', 'ruby', 'perl', 'go',
    'rust', 'scala', 'typescript', 'html', 'css', 'api', 'ml', 'ai', 'nlp',
    'aws', 'azure', 'gcp', 'docker', 'kubernetes', 'git', 'github', 'gitlab',
    'linux', 'unix', 'windows', 'macos', 'android', 'ios', 'firebase', 'mongodb',
    'mysql', 'postgresql', 'sqlite', 'django', 'flask', 'spring', '.net',
    'tensorflow', 'pytorch', 'keras', 'scikit-learn', 'pandas', 'numpy'
}

# NEW: List of junk words to ignore in job descriptions
JOB_JUNK_WORDS = {
    'role', 'experience', 'responsibilities', 'requirements', 'qualifications',
    'skill', 'skills', 'degree', 'team', 'company', 'work', 'job', 'description',
    'profile', 'position', 'opportunity', 'candidate', 'ability', 'knowledge',
    'understanding', 'education', 'background', 'familiarity'
}

# --- UPDATED: Smarter Keyword Extractor ---
def extract_keywords(text):
    """Extracts keywords, filtering out junk words."""
    doc = nlp(text)
    keywords = set()
    for token in doc:
        word = token.lemma_.lower()
        if (
            not token.is_stop and
            not token.is_punct and
            word not in JOB_JUNK_WORDS and  # Check against junk list
            token.pos_ in ['NOUN', 'PROPN', 'ADJ']
        ):
            keywords.add(word)
    return list(keywords)

# --- UPDATED: Smarter Named Entity Recognition (NER) Function ---
def extract_entities(text):
    """Uses SpaCy's NER model, but filters out common tech jargon."""
    doc = nlp(text)
    entities = {
        "Companies / Organizations": set(),
        "Locations": set()
    }
    
    for ent in doc.ents:
        # Check if the entity is in our tech jargon list
        if ent.text.lower() not in TECH_JARGON:
            if ent.label_ == "ORG":
                entities["Companies / Organizations"].add(ent.text)
            elif ent.label_ == "GPE":
                entities["Locations"].add(ent.text)
            
    # Convert sets to lists for display
    return {
        "Companies / Organizations": list(entities["Companies / Organizations"]),
        "Locations": list(entities["Locations"])
    }

def match_resume_to_job(resume_text, job_keywords):
    resume_text_lower = resume_text.lower()
    found_keywords = []
    missing_keywords = []
    
    for keyword in job_keywords:
        if keyword in resume_text_lower:
            found_keywords.append(keyword)
        else:
            missing_keywords.append(keyword)
            
    if not job_keywords:
        return 0, []
        
    match_score = int((len(found_keywords) / len(job_keywords)) * 100)
    return match_score, missing_keywords

def get_linkedin_feedback(about_text, skills_text):
    suggestions = []
    score = 0
    
    cleaned_text = re.sub(r'[^a-zA-Z\s]', '', about_text).lower()
    words = cleaned_text.split()
    
    if len(words) > 50: score += 30
    else: suggestions.append(f"* **About Section is too short:** Yours is {len(words)} words. Aim for 50+.")
    
    action_word_count = sum(1 for word in words if word in POWER_WORDS)
    if action_word_count >= 3: score += 30
    else: suggestions.append(f"* **Add Action Verbs:** Your 'About' section has {action_word_count} action verbs. Aim for 3 or more.")

    skills_list = [skill.strip().lower() for skill in skills_text.split(',')]
    skills_count = len(skills_list) if skills_text else 0

    if skills_count >= 5: score += 20
    if skills_count >= 10: score += 20
    if skills_count < 5: suggestions.append(f"* **Add more skills:** You listed {skills_count} skills. Aim for at least 5-10.")
        
    return suggestions, score

def get_resume_feedback(resume_text):
    suggestions = []
    score = 0
    
    cleaned_text = re.sub(r'[^a-zA-Z\s]', '', resume_text).lower()
    words = cleaned_text.split()
    
    if len(words) > 150: score += 20
    else: suggestions.append(f"* **Resume seems short:** Yours is {len(words)} words.")

    action_word_count = sum(1 for word in words if word in POWER_WORDS)
    
    if action_word_count >= 3: score += 30
    if action_word_count >= 5: score += 20
    if action_word_count < 3: suggestions.append(f"* **Add action verbs:** You used {action_word_count} action verbs. Aim for at least 3.")
    
    if 'education' in cleaned_text: score += 15
    else: suggestions.append("* **'Education' section not found.**")
        
    if 'experience' in cleaned_text: score += 15
    else: suggestions.append("* **'Experience' section not found.**")
        
    return suggestions, score

def create_score_chart(score, title):
    if score == 100:
        fig = go.Figure(go.Pie(values=[100], labels=['Perfect Score!'], marker_colors=['#00C853']))
    else:
        fig = go.Figure(go.Pie(
            values=[score, 100 - score],
            labels=['Your Score', 'Points to Improve'],
            marker_colors=['#00C853', '#FFD600'],
            hole=0.4, textinfo='percent'
        ))
    
    fig.update_layout(
        title_text=f'<b>{title}</b>',
        annotations=[dict(text=f'<b>{score}/100</b>', x=0.5, y=0.5, font_size=20, showarrow=False)],
        showlegend=False, height=300, margin=dict(t=50, b=0, l=0, r=0)
    )
    return fig

def get_summary_line(score, context="profile"):
    if score == 100: st.success(f"🎉 **Perfect! 100/100. Your {context} is in excellent shape!**")
    elif score >= 80: st.success(f"🚀 **Very Good! {score}/100. Your {context} is strong.**")
    elif score >= 60: st.warning(f"👍 **Good Start! {score}/100. Follow the tips below to improve.**")
    else: st.error(f"🌱 **Needs Work. {score}/100. Let's get this score up!**")

# --- Main App Logic ---

st.sidebar.title('Navigation')
app_mode = st.sidebar.radio(
    "Choose an Analyzer",
    ("LinkedIn Analyzer", "Resume Analyzer")
)

# --- LinkedIn Analyzer Page ---
if app_mode == "LinkedIn Analyzer":
    st.sidebar.header("LinkedIn Inputs")
    about_input = st.sidebar.text_area("Paste your 'About' Section", height=150)
    skills_input = st.sidebar.text_input("Paste your 'Skills' (comma-separated)", "e.g., Python, SQL, Streamlit")
    
    if st.sidebar.button("Analyze LinkedIn Profile"):
        if not about_input or not skills_input:
            st.sidebar.error("Please paste both your 'About' and 'Skills' sections.")
        else:
            st.header('LinkedIn Profile Analysis')
            with st.spinner('Analyzing your profile...'):
                suggestions, score = get_linkedin_feedback(about_input, skills_input)
                
                get_summary_line(score, "profile")
                fig = create_score_chart(score, 'LinkedIn Profile Score')
                st.plotly_chart(fig, use_container_width=True)
                
                st.subheader('Your Action Plan')
                if suggestions:
                    st.markdown('\n'.join(suggestions))
                else:
                    st.success("**✅ Your profile summary looks strong!**")

# --- Resume Analyzer Page ---
elif app_mode == "Resume Analyzer":
    st.sidebar.header("Resume Inputs")
    resume_file = st.sidebar.file_uploader('Upload your resume (PDF)', type='pdf', key="resume_uploader")
    job_desc_input = st.sidebar.text_area("Paste the Job Description", height=150)
    
    if st.sidebar.button("Analyze Resume for Job"):
        if resume_file and job_desc_input:
            st.header('Resume & Job Match Analysis')
            with st.spinner('Analyzing...'):
                resume_text = extract_text_from_pdf(resume_file)
                if resume_text:
                    # --- 1. General Resume Analysis ---
                    st.subheader("General Resume Score")
                    suggestions, score = get_resume_feedback(resume_text)
                    
                    get_summary_line(score, "resume")
                    fig = create_score_chart(score, 'General Resume Score')
                    st.plotly_chart(fig, use_container_width=True)
                    
                    st.subheader('General Action Plan')
                    if suggestions:
                        st.markdown('\n'.join(suggestions))
                    
                    st.divider()
                    
                    # --- 2. Key Entities Section (UPDATED) ---
                    st.subheader("Key Entities Detected (NER Scan)")
                    with st.spinner("Scanning for entities..."):
                        entities = extract_entities(resume_text)
                        
                        if not entities["Companies / Organizations"] and not entities["Locations"]:
                            st.info("No major entities (company names or locations) were automatically detected.")
                        else:
                            if entities["Companies / Organizations"]:
                                st.markdown("**Skills, Companies & Organizations:**")
                                st.markdown(f"```\n{', '.join(entities['Companies / Organizations'])}\n```")
                            if entities["Locations"]:
                                st.markdown("**Locations:**")
                                st.markdown(f"```\n{', '.join(entities['Locations'])}\n```")

                    st.divider()
                    
                    # --- 3. Job Match Analysis ---
                    st.subheader("Job Match Score")
                    job_keywords = extract_keywords(job_desc_input)
                    match_score, missing_keywords = match_resume_to_job(resume_text, job_keywords)
                    
                    get_summary_line(match_score, "job match")
                    fig_match = create_score_chart(match_score, 'Job Match Score')
                    st.plotly_chart(fig_match, use_container_width=True)
                    
                    if missing_keywords:
                        st.subheader('Missing Keywords to Add')
                        st.warning("Your resume appears to be missing these keywords from the job description:")
                        st.markdown('\n'.join(f'* `{kw}`' for kw in missing_keywords))
                    else:
                        st.success("**✅ Your resume contains all the major keywords!**")
                else:
                    st.error("Could not read text from the uploaded PDF.")
        else:
            st.sidebar.error("Please upload a resume AND paste a job description.")