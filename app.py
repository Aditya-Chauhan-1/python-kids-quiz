
import streamlit as st

st.set_page_config(
    page_title="Python Quiz for Kids",
    page_icon="🐍",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap');

.stApp {
    background: linear-gradient(135deg, #eef2ff 0%, #f5f3ff 50%, #ecfeff 100%);
}

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
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
    max-width: 850px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

.hero {
    background: linear-gradient(135deg, #312e81, #4f46e5, #0891b2);
    padding: 35px 25px;
    border-radius: 24px;
    text-align: center;
    color: white;
    box-shadow: 0 12px 30px rgba(79,70,229,0.22);
    margin-bottom: 22px;
}

.hero h1 {
    color: white;
    font-size: clamp(27px, 5vw, 42px);
    font-weight: 800;
    margin: 8px 0;
}

.hero p {
    color: #e0e7ff;
    font-size: 15px;
    margin-bottom: 0;
}

.hero-icon {
    font-size: 46px;
}

.badge {
    display: inline-block;
    background: rgba(255,255,255,0.17);
    border: 1px solid rgba(255,255,255,0.25);
    padding: 6px 14px;
    border-radius: 30px;
    font-size: 12px;
    font-weight: 600;
}

.info-card {
    background: white;
    padding: 17px;
    border-radius: 16px;
    border: 1px solid #e0e7ff;
    box-shadow: 0 5px 15px rgba(30,41,59,0.05);
    text-align: center;
    margin-bottom: 22px;
}

.info-card h3 {
    color: #4338ca;
    font-size: 22px;
    margin: 0;
}

.info-card p {
    color: #64748b;
    font-size: 12px;
    margin: 3px 0 0;
}

.section-title {
    color: #312e81;
    font-size: 22px;
    font-weight: 800;
    margin: 20px 0 8px;
}

.question-card {
    background: white;
    padding: 18px 20px;
    border: 1px solid #e2e8f0;
    border-radius: 17px;
    margin: 15px 0 8px;
    box-shadow: 0 5px 16px rgba(15,23,42,0.045);
}

div[data-testid="stRadio"] label {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 10px;
    padding: 8px 12px;
    margin: 4px 0;
    transition: all 0.2s ease;
}

div[data-testid="stRadio"] label:hover {
    background: #eef2ff;
    border-color: #818cf8;
}

.stTextInput input {
    border-radius: 12px;
    border: 1px solid #c7d2fe;
    padding: 12px;
}

.stTextInput input:focus {
    border-color: #6366f1;
    box-shadow: 0 0 0 2px #c7d2fe;
}

.stButton button,
.stFormSubmitButton button {
    background: linear-gradient(135deg, #4f46e5, #7c3aed);
    color: white !important;
    border: none;
    border-radius: 12px;
    padding: 12px;
    font-weight: 700;
    min-height: 48px;
    transition: 0.2s ease;
}

.stButton button:hover,
.stFormSubmitButton button:hover {
    background: linear-gradient(135deg, #4338ca, #6d28d9);
    transform: translateY(-1px);
}

.result-card {
    background: white;
    border: 1px solid #c7d2fe;
    border-radius: 22px;
    padding: 25px;
    text-align: center;
    box-shadow: 0 8px 25px rgba(79,70,229,0.12);
    margin-top: 25px;
}

.result-card h2 {
    color: #312e81;
}

.footer-text {
    text-align: center;
    color: #64748b;
    font-size: 12px;
    margin-top: 30px;
}

@media (max-width: 600px) {
    .block-container {
        padding: 1rem 0.8rem 2rem;
    }

    .hero {
        padding: 25px 15px;
        border-radius: 18px;
    }

    .question-card {
        padding: 14px;
    }
}
</style>
""", unsafe_allow_html=True)

# ---------------- HERO HEADER ----------------
st.markdown("""
<div class="hero">
    <div class="badge">✨ LEARN • THINK • CODE</div>
    <div class="hero-icon">🐍</div>
    <h1>Python Quiz for Kids</h1>
    <p>Challenge your coding skills and become a Python Star!</p>
</div>
""", unsafe_allow_html=True)

# ---------------- QUIZ INFORMATION ----------------
st.markdown("""
<div class="info-card">
    <h3>🎯 Your Coding Challenge</h3>
    <p>10 Questions &nbsp; • &nbsp; 10 Marks &nbsp; • &nbsp; Beginner Level</p>
</div>
""", unsafe_allow_html=True)

# ---------------- STUDENT DETAILS ----------------
st.markdown('<div class="section-title">👨‍🎓 Student Details</div>',
            unsafe_allow_html=True)

student_name = st.text_input(
    "Your Name",
    placeholder="Enter your full name",
    key="student_name"
)

# ---------------- QUESTIONS ----------------
questions = [
    {
        "q": "Which function displays output in Python?",
        "options": ["display()", "print()", "show()", "write()"],
        "answer": "print()"
    },
    {
        "q": "What is the correct file extension for Python files?",
        "options": [".pt", ".pyt", ".py", ".python"],
        "answer": ".py"
    },
    {
        "q": "Which of these is a valid variable name in Python?",
        "options": ["2myvar", "my_var", "my-var", "my var"],
        "answer": "my_var"
    },
    {
        "q": "What is the output of 5 + 2 * 3?",
        "options": ["21", "11", "16", "25"],
        "answer": "11"
    },
    {
        "q": "Which data type is used to store text in Python?",
        "options": ["int", "float", "str", "bool"],
        "answer": "str"
    },
    {
        "q": "How do you start a single-line comment in Python?",
        "options": ["//", "/*", "#", "--"],
        "answer": "#"
    },
    {
        "q": "Which collection type is ordered and changeable (mutable)?",
        "options": ["List", "Tuple", "Set", "Dictionary Keys"],
        "answer": "List"
    },
    {
        "q": "Which keyword is used to define a function in Python?",
        "options": ["func", "def", "function", "define"],
        "answer": "def"
    },
    {
        "q": "Which operator is used for equality comparison?",
        "options": ["=", "==", "===", "!="],
        "answer": "=="
    },
    {
        "q": "What will type(10.5) return?",
        "options": [
            "<class 'int'>",
            "<class 'float'>",
            "<class 'str'>",
            "<class 'number'>"
        ],
        "answer": "<class 'float'>"
    }
]

st.markdown('<div class="section-title">📝 Answer All Questions</div>',
            unsafe_allow_html=True)

st.caption("Choose one correct answer for each question.")

# ---------------- QUIZ FORM ----------------
with st.form("python_quiz_form"):
    user_answers = {}

    for i, q_data in enumerate(questions):
        st.markdown(
            f'<div class="question-card">'
            f'<strong style="color:#4f46e5;">QUESTION {i+1:02d} / 10</strong>'
            f'<p style="color:#1e293b;font-size:16px;font-weight:600;'
            f'margin:10px 0 0;">{q_data["q"]}</p></div>',
            unsafe_allow_html=True
        )

        user_answers[i] = st.radio(
            f"Choose your answer for question {i+1}",
            options=q_data["options"],
            index=None,
            key=f"answer_{i}",
            label_visibility="collapsed"
        )

    submitted = st.form_submit_button(
        "🚀 Submit My Quiz",
        use_container_width=True
    )

# ---------------- RESULTS ----------------
if submitted:
    if not student_name.strip():
        st.warning("⚠️ Please enter your name before submitting.")

    elif any(user_answers[i] is None for i in range(len(questions))):
        unanswered = sum(
            1 for i in range(len(questions))
            if user_answers[i] is None
        )
        st.warning(
            f"📝 You still have {unanswered} unanswered question(s). "
            "Please answer all questions."
        )

    else:
        score = sum(
            1 for i, q_data in enumerate(questions)
            if user_answers[i] == q_data["answer"]
        )

        percentage = (score / len(questions)) * 100

        if score >= 9:
            emoji = "🏆"
            result_title = "Python Champion!"
            message = "Outstanding! You are a Python superstar!"
        elif score >= 7:
            emoji = "🌟"
            result_title = "Excellent Work!"
            message = "Great job! Keep practicing to master Python."
        elif score >= 5:
            emoji = "👏"
            result_title = "Good Effort!"
            message = "You are learning! Practice a little more."
        else:
            emoji = "💪"
            result_title = "Keep Learning!"
            message = "Don't give up. Learn, practice, and try again!"

        st.markdown(
            f"""
            <div class="result-card">
                <div style="font-size:55px;">{emoji}</div>
                <h2>{result_title}</h2>
                <p style="color:#64748b;">Well done, {student_name.strip()}!</p>
                <p style="font-size:48px;font-weight:800;color:#4f46e5;
                margin:8px 0;">{score} / {len(questions)}</p>
                <p style="font-size:18px;font-weight:600;color:#0891b2;">
                {percentage:.0f}% Score</p>
                <p style="color:#475569;">{message}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Correct Answers", f"{score}/10")

        with col2:
            st.metric("Incorrect Answers", f"{10-score}/10")

        st.progress(percentage / 100)

        with st.expander("📚 Review Your Answers"):
            for i, q_data in enumerate(questions):
                selected = user_answers[i]
                correct = q_data["answer"]

                if selected == correct:
                    st.success(
                        f"Q{i+1}. {q_data['q']}\n\n"
                        f"Your answer: {selected} ✓"
                    )
                else:
                    st.error(
                        f"Q{i+1}. {q_data['q']}\n\n"
                        f"Your answer: {selected}\n\n"
                        f"Correct answer: {correct}"
                    )

        if score >= 8:
            st.balloons()

        if st.button("🔄 Try Again", use_container_width=True):
            st.rerun()

# ---------------- FOOTER ----------------
st.markdown("""
<div class="footer-text">
    💻 Made with Python & Streamlit<br>
    Keep Learning • Keep Coding • Keep Growing 🚀
</div>
""", unsafe_allow_html=True)
