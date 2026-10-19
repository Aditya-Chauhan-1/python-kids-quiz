import streamlit as st

st.set_page_config(
    page_title="Python Champions Quiz",
    page_icon="https://www.python.org/static/favicon.ico",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Fira+Code:wght@400;600&display=swap');

html, body, [class*="css"], .stApp {
    font-family: 'Plus Jakarta Sans', sans-serif;
    background: radial-gradient(circle at top, #eef2ff 0%, #f8fafc 100%);
}

#MainMenu, footer, header,
[data-testid="stHeader"],
[data-testid="stToolbar"],
[data-testid="stStatusWidget"],
[data-testid="manage-app-button"],
.stAppDeployButton {
    display: none !important;
}

.block-container {
    max-width: 820px;
    padding-top: 1.5rem;
    padding-bottom: 3rem;
}

/* Hero Card */
.hero-card {
    background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
    border: 1px solid rgba(255, 255, 255, 0.12);
    border-radius: 28px;
    padding: 36px 24px;
    text-align: center;
    color: white;
    box-shadow: 0 20px 40px rgba(15, 23, 42, 0.18);
    margin-bottom: 24px;
}

.python-logo-wrapper {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 84px;
    height: 84px;
    background: rgba(255, 255, 255, 0.08);
    border: 1px solid rgba(255, 255, 255, 0.18);
    border-radius: 24px;
    backdrop-filter: blur(10px);
    margin-bottom: 12px;
}

.python-logo-img {
    width: 52px;
    height: 52px;
    filter: drop-shadow(0 4px 10px rgba(0,0,0,0.3));
}

.badge-tag {
    display: inline-block;
    background: linear-gradient(90deg, #38bdf8, #818cf8);
    color: #0f172a;
    padding: 6px 16px;
    border-radius: 999px;
    font-size: 12px;
    font-weight: 800;
    letter-spacing: 0.5px;
    margin-bottom: 12px;
}

.hero-card h1 {
    font-size: clamp(28px, 4vw, 40px);
    font-weight: 800;
    margin: 8px 0;
    background: linear-gradient(120deg, #ffffff 40%, #93c5fd);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-card p {
    color: #94a3b8;
    font-size: 15px;
    margin-bottom: 0;
}

/* Stat bar */
.quiz-meta-bar {
    display: flex;
    justify-content: space-around;
    background: white;
    border: 1px solid #e2e8f0;
    border-radius: 20px;
    padding: 16px;
    margin-bottom: 24px;
    box-shadow: 0 6px 20px rgba(15, 23, 42, 0.03);
}

.meta-item {
    text-align: center;
}

.meta-item .num {
    font-size: 20px;
    font-weight: 800;
    color: #2563eb;
}

.meta-item .label {
    font-size: 12px;
    color: #64748b;
    font-weight: 600;
}

/* Question Box */
.q-box {
    background: white;
    border: 1px solid #e2e8f0;
    border-radius: 20px;
    padding: 20px 22px;
    margin-bottom: 16px;
    box-shadow: 0 4px 16px rgba(15, 23, 42, 0.03);
}

.q-badge {
    display: inline-block;
    background: #eff6ff;
    color: #2563eb;
    border: 1px solid #bfdbfe;
    padding: 4px 10px;
    border-radius: 8px;
    font-size: 12px;
    font-weight: 700;
    margin-bottom: 8px;
}

.q-title {
    color: #1e293b;
    font-size: 17px;
    font-weight: 700;
    margin: 4px 0 12px;
}

/* Radio button styles - FIXED */
div[data-testid="stRadio"] > div[role="radiogroup"] {
    display: flex;
    flex-direction: column;
    gap: 10px;
    width: 100%;
}

div[data-testid="stRadio"] label[data-baseweb="radio"] {
    background: #ffffff !important;
    border: 1.5px solid #cbd5e1 !important;
    border-radius: 12px !important;
    padding: 10px 16px !important;
    margin: 0 !important;
    width: 100% !important;
    display: flex !important;
    align-items: center !important;
    cursor: pointer !important;
    transition: all 0.2s ease !important;
}

div[data-testid="stRadio"] label[data-baseweb="radio"]:hover {
    background: #eff6ff !important;
    border-color: #3b82f6 !important;
}

div[data-testid="stRadio"] label[data-baseweb="radio"] div,
div[data-testid="stRadio"] label[data-baseweb="radio"] p,
div[data-testid="stRadio"] label[data-baseweb="radio"] span {
    color: #0f172a !important;
    font-size: 15px !important;
    font-weight: 600 !important;
    opacity: 1 !important;
    visibility: visible !important;
}

/* Text input */
.stTextInput input {
    border-radius: 14px;
    border: 1.5px solid #cbd5e1;
    padding: 12px 14px;
    font-size: 15px;
}

.stTextInput input:focus {
    border-color: #3b82f6;
    box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.15);
}

/* Buttons */
.stButton button,
.stFormSubmitButton button {
    background: linear-gradient(135deg, #2563eb 0%, #4f46e5 100%);
    color: white !important;
    border: none;
    border-radius: 14px;
    padding: 14px;
    font-size: 16px;
    font-weight: 700;
    min-height: 52px;
    box-shadow: 0 10px 20px rgba(37, 99, 235, 0.25);
    transition: transform 0.15s ease;
}

.stButton button:hover,
.stFormSubmitButton button:hover {
    transform: translateY(-2px);
    box-shadow: 0 14px 26px rgba(37, 99, 235, 0.35);
}

.popup-score-badge {
    font-size: 42px;
    font-weight: 800;
    color: #2563eb;
    margin: 8px 0;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HERO HEADER ----------------
st.markdown("""
<div class="hero-card">
    <div class="badge-tag">⚡ CODING CHALLENGE FOR JUNIOR PROS</div>
    <br>
    <div class="python-logo-wrapper">
        <img class="python-logo-img" 
             src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" 
             alt="Python Official Logo">
    </div>
    <h1>Python Star Quiz</h1>
    <p>Loops, Conditions, Dictionaries, Lists & Functions — Let's check your coding powers!</p>
</div>
""", unsafe_allow_html=True)

# ---------------- QUIZ META BAR ----------------
st.markdown("""
<div class="quiz-meta-bar">
    <div class="meta-item">
        <div class="num">10</div>
        <div class="label">Questions</div>
    </div>
    <div class="meta-item">
        <div class="num">10</div>
        <div class="label">Total Points</div>
    </div>
    <div class="meta-item">
        <div class="num">Kids & Beginners</div>
        <div class="label">Level</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ---------------- STUDENT DETAILS ----------------
student_name = st.text_input(
    "Coder Name",
    placeholder="Type your name here...",
    key="student_name"
)

# ---------------- QUESTIONS LIST ----------------
questions = [
    {
        "q": "What will be the output of this code?",
        "code": "nums = [10, 20, 30]\nprint(nums[1])",
        "options": ["10", "20", "30", "IndexError"],
        "answer": "20",
        "topic": "List Indexing"
    },
    {
        "q": "How many times will this `for` loop print 'Python'?",
        "code": "for i in range(3):\n    print('Python')",
        "options": ["2 times", "3 times", "4 times", "Infinite"],
        "answer":
