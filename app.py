import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Python Quiz for Kids",
    page_icon="🐍",
    layout="centered"
)

# Manage app, footer aur header hide karne ke liye CSS
hide_elements = """
<style>
/* Right side 'Manage app' button hide */
[data-testid="manage-app-button"] {
    display: none !important;
}

/* Footer aur Streamlit branding hide */
footer {
    visibility: hidden;
    height: 0%;
}

/* Status widget aur deploy button hide */
div[data-testid="stStatusWidget"] {
    display: none !important;
}
.stAppDeployButton {
    display: none !important;
}

/* Top toolbar / header menu hide */
header {
    visibility: hidden !important;
    height: 0%;
}

/* Custom styling for card box */
.quiz-card {
    background-color: #1e293b;
    padding: 20px;
    border-radius: 10px;
    border: 1px solid #334155;
    margin-bottom: 20px;
}
</style>
"""
st.markdown(hide_elements, unsafe_allow_html=True)

# Header Section
st.title("🐍 Python Quiz for Kids")
st.write("Test your Python knowledge!")

st.info("Total Questions: 10 | Each Question: 1 Mark")

# Student Details
student_name = st.text_input("Student Name", placeholder="Enter your full name")

st.markdown("### 📝 Answer All Questions")

# Questions Data
questions = [
    {
        "q": "1. Which function displays output in Python?",
        "options": ["display()", "print()", "show()", "write()"],
        "answer": "print()"
    },
    {
        "q": "2. What is the correct file extension for Python files?",
        "options": [".pt", ".pyt", ".py", ".python"],
        "answer": ".py"
    },
    {
        "q": "3. Which of these is a valid variable name in Python?",
        "options": ["2myvar", "my_var", "my-var", "my var"],
        "answer": "my_var"
    },
    {
        "q": "4. What is the output of 5 + 2 * 3?",
        "options": ["21", "11", "16", "25"],
        "answer": "11"
    },
    {
        "q": "5. Which data type is used to store text in Python?",
        "options": ["int", "float", "str", "bool"],
        "answer": "str"
    },
    {
        "q": "6. How do you start a single-line comment in Python?",
        "options": ["//", "/*", "#", "--"],
        "answer": "#"
    },
    {
        "q": "7. Which collection type is ordered and changeable (mutable)?",
        "options": ["List", "Tuple", "Set", "Dictionary Keys"],
        "answer": "List"
    },
    {
        "q": "8. What is the keyword used to define a function in Python?",
        "options": ["func", "def", "function", "define"],
        "answer": "def"
    },
    {
        "q": "9. Which operator is used for equal comparison?",
        "options": ["=", "==", "===", "!="],
        "answer": "=="
    },
    {
        "q": "10. What will `type(10.5)` return?",
        "options": ["<class 'int'>", "<class 'float'>", "<class 'str'>", "<class 'number'>"],
        "answer": "<class 'float'>"
    }
]

# Form handling
with st.form("quiz_form"):
    user_answers = {}
    for i, q_data in enumerate(questions):
        st.write(f"**{q_data['q']}**")
        user_answers[i] = st.radio(
            label=f"Options for question {i+1}",
            options=q_data["options"],
            index=None,
            key=f"q_{i}",
            label_visibility="collapsed"
        )
        st.write("---")

    submitted = st.form_submit_button("Submit Quiz", use_container_width=True)

# Results
if submitted:
    if not student_name.strip():
        st.warning("⚠️ Please enter your name before submitting.")
    else:
        score = 0
        for i, q_data in enumerate(questions):
            if user_answers.get(i) == q_data["answer"]:
                score += 1

        st.success(f"🎉 Well done, {student_name}! You scored **{score} / {len(questions)}**")
        
        if score >= 8:
            st.balloons()
