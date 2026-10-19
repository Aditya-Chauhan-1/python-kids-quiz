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
    position: relative;
    overflow: hidden;
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

/* Fix for Radio Buttons and Text Visibility */
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

/* Ensure text is clearly visible and dark */
div[data-testid="stRadio"] label[data-baseweb="radio"] div,
div[data-testid="stRadio"] label[data-baseweb="radio"] p,
div[data-testid="stRadio"] label[data-baseweb="radio"] span {
    color: #0f172a !important;
    font-size: 15px !important;
    font-weight: 600 !important;
    opacity: 1 !important;
    visibility: visible !important;
}

div[data-testid="stRadio"] label:hover {
    background: #f1f5f9;
    border-color: #3b82f6;
    transform: translateX(3px);
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

# ---------------- HERO HEADER (WITH PYTHON LOGO) ----------------
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
        "answer": "3 times",
        "topic": "For Loop"
    },
    {
        "q": "What will this condition print?",
        "code": "age = 10\nif age >= 12:\n    print('Teen')\nelse:\n    print('Kid')",
        "options": ["Teen", "Kid", "10", "Error"],
        "answer": "Kid",
        "topic": "If-Else Condition"
    },
    {
        "q": "What value will be printed from this dictionary?",
        "code": "student = {'name': 'Aarav', 'marks': 95}\nprint(student['marks'])",
        "options": ["name", "Aarav", "95", "{'marks': 95}"],
        "answer": "95",
        "topic": "Dictionary"
    },
    {
        "q": "What is the output of this function call?",
        "code": "def add(a, b):\n    return a + b\n\nprint(add(4, 5))",
        "options": ["9", "45", "None", "Error"],
        "answer": "9",
        "topic": "Functions"
    },
    {
        "q": "What will be printed when this while loop terminates?",
        "code": "count = 1\nwhile count < 3:\n    count += 1\nprint(count)",
        "options": ["1", "2", "3", "4"],
        "answer": "3",
        "topic": "While Loop"
    },
    {
        "q": "Which method adds a new item to the end of a list?",
        "code": "fruits = ['apple', 'banana']\n# Add 'mango' to list",
        "options": ["fruits.add('mango')", "fruits.append('mango')", "fruits.push('mango')", "fruits.insert_end('mango')"],
        "answer": "fruits.append('mango')",
        "topic": "List Methods"
    },
    {
        "q": "What will this dictionary operation display?",
        "code": "scores = {'math': 90}\nscores['science'] = 85\nprint(len(scores))",
        "options": ["1", "2", "85", "175"],
        "answer": "2",
        "topic": "Dictionary Mutability"
    },
    {
        "q": "What will this loop with range() print?",
        "code": "total = 0\nfor x in [1, 2, 3]:\n    total = total + x\nprint(total)",
        "options": ["3", "5", "6", "123"],
        "answer": "6",
        "topic": "Accumulator Pattern"
    },
    {
        "q": "What does this function print?",
        "code": "def greet(name='Coder'):\n    print('Hello ' + name)\n\ngreet()",
        "options": ["Hello", "Hello name", "Hello Coder", "Error"],
        "answer": "Hello Coder",
        "topic": "Default Arguments"
    }
]

# ---------------- RESULT POPUP DIALOG ----------------
@st.dialog("🎯 Quiz Results Summary", width="large")
def show_result_popup(name, score, total_q, answers_map):
    pct = (score / total_q) * 100

    if score >= 9:
        badge_icon = "🏆"
        title = "Python Superstar!"
        note = "Sensational performance! You have nailed all the core concepts."
    elif score >= 7:
        badge_icon = "🌟"
        title = "Great Job, Young Coder!"
        note = "Super impressive! With just a bit more practice, you'll be unstoppable."
    elif score >= 5:
        badge_icon = "🚀"
        title = "Good Attempt!"
        note = "You know your basics well! Keep practicing loops and dictionaries."
    else:
        badge_icon = "💡"
        title = "Keep Practicing!"
        note = "Don't give up! Go through the review section below to master these questions."

    st.markdown(
        f"""
        <div style="text-align: center; padding: 10px 0;">
            <div style="font-size: 50px;">{badge_icon}</div>
            <h2 style="color: #1e293b; margin: 4px 0;">{title}</h2>
            <p style="color: #64748b; font-size: 15px;">Congratulations, <b>{name}</b>!</p>
            <div class="popup-score-badge">{score} / {total_q}</div>
            <p style="font-weight: 700; color: #0284c7; font-size: 16px;">Accuracy: {pct:.0f}%</p>
            <p style="color: #475569; font-size: 14px; max-width: 480px; margin: 0 auto 16px;">{note}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    c1, c2 = st.columns(2)
    c1.metric("Correct Answers", f"{score}")
    c2.metric("Mistakes", f"{total_q - score}")

    st.markdown("---")
    st.markdown("### 🔍 Answer Review")

    for i, q in enumerate(questions):
        user_choice = answers_map[i]
        is_correct = (user_choice == q["answer"])
        status = "✅ Correct" if is_correct else "❌ Incorrect"
        
        with st.expander(f"Q{i+1}: {q['topic']} — {status}"):
            if q["code"]:
                st.code(q["code"], language="python")
            st.markdown(f"**Your Choice:** `{user_choice}`")
            if not is_correct:
                st.markdown(f"**Correct Answer:** `{q['answer']}`")

    if st.button("Close & Continue", use_container_width=True):
        st.rerun()

# ---------------- MAIN QUIZ FORM ----------------
with st.form("quiz_form"):
    answers = {}

    for i, q_data in enumerate(questions):
        st.markdown(f"""
        <div class="q-box">
            <span class="q-badge">Question {i+1} of 10 • {q_data['topic']}</span>
            <div class="q-title">{q_data['q']}</div>
        </div>
        """, unsafe_allow_html=True)

        if q_data["code"]:
            st.code(q_data["code"], language="python")

        answers[i] = st.radio(
            label=f"Options for question {i+1}",
            options=q_data["options"],
            index=None,
            key=f"q_radio_{i}",
            label_visibility="collapsed"
        )
        st.write("")

    submitted = st.form_submit_button("🚀 Submit Quiz & View Result", use_container_width=True)

# ---------------- FORM PROCESSING ----------------
if submitted:
    if not student_name.strip():
        st.error("⚠️ Please enter your name at the top before submitting.")
    elif any(answers[i] is None for i in range(len(questions))):
        unanswered = sum(1 for i in range(len(questions)) if answers[i] is None)
        st.warning(f"⚠️ You still have {unanswered} question(s) left. Attempt all before finishing!")
    else:
        final_score = sum(1 for i, q in enumerate(questions) if answers[i] == q["answer"])
        if final_score >= 8:
            st.balloons()
        # Open Modal Dialog Popup
        show_result_popup(student_name.strip(), final_score, len(questions), answers)

# ---------------- FOOTER ----------------
st.markdown("""
<div style="text-align: center; color: #94a3b8; font-size: 13px; margin-top: 40px;">
    Crafted for future developers • Built with Python & Streamlit
</div>
""", unsafe_allow_html=True)
