
import streamlit as st

st.set_page_config(
    page_title="Python Quiz for Kids",
    page_icon="🐍",
    layout="centered"
)

st.title("🐍 Python Quiz for Kids")
st.write("Test your Python knowledge!")
st.info("Total Questions: 10 | Each Question: 1 Mark")

questions = [
    {
        "question": "1. Which function displays output in Python?",
        "options": ["input()", "print()", "type()", "int()"],
        "answer": "print()"
    },
    {
        "question": "2. Which symbol is used for comments in Python?",
        "options": ["//", "<!-- -->", "#", "**"],
        "answer": "#"
    },
    {
        "question": "3. Which data type stores whole numbers?",
        "options": ["str", "int", "list", "bool"],
        "answer": "int"
    },
    {
        "question": "4. What is the output of 5 + 3?",
        "options": ["53", "8", "2", "15"],
        "answer": "8"
    },
    {
        "question": "5. Which keyword checks a condition?",
        "options": ["for", "print", "if", "def"],
        "answer": "if"
    },
    {
        "question": "6. Which symbol is used for multiplication?",
        "options": ["x", "*", "/", "%"],
        "answer": "*"
    },
    {
        "question": "7. Which data type stores True or False?",
        "options": ["int", "str", "float", "bool"],
        "answer": "bool"
    },
    {
        "question": "8. Which loop can repeat code a fixed number of times?",
        "options": ["for", "print", "input", "if"],
        "answer": "for"
    },
    {
        "question": "9. Which function takes input from the user?",
        "options": ["print()", "input()", "range()", "type()"],
        "answer": "input()"
    },
    {
        "question": "10. What is the output of 10 // 3?",
        "options": ["3", "3.33", "1", "0"],
        "answer": "3"
    }
]

with st.form("python_quiz_form"):
    name = st.text_input("Student Name")

    st.subheader("📝 Answer All Questions")

    answers = []

    for q in questions:
        st.write("---")
        st.write(q["question"])

        selected = st.radio(
            "Choose your answer:",
            q["options"],
            index=None,
            key=q["question"]
        )
        answers.append(selected)

    submitted = st.form_submit_button(
        "Submit Quiz",
        type="primary",
        use_container_width=True
    )

if submitted:
    if not name.strip():
        st.warning("Please enter your name.")
    elif any(answer is None for answer in answers):
        st.warning("Please answer all 10 questions.")
    else:
        score = sum(
            1 for i, q in enumerate(questions)
            if answers[i] == q["answer"]
        )

        percentage = score * 10

        st.success("Quiz submitted successfully!")

        st.subheader(f"🎉 Well done, {name}!")

        col1, col2 = st.columns(2)
        col1.metric("Your Score", f"{score}/10")
        col2.metric("Percentage", f"{percentage}%")

        if score >= 8:
            st.balloons()
            st.success("Excellent! You are a Python Star! 🌟")
        elif score >= 5:
            st.info("Good job! Keep practicing! 👍")
        else:
            st.warning("Keep learning. You can do it! 💪")

        with st.expander("📖 View Correct Answers"):
            for i, q in enumerate(questions):
                st.write(f"**{i+1}. {q['question']}**")
                st.write(f"Your answer: {answers[i]}")
                st.write(f"Correct answer: {q['answer']}")

        st.caption("Thank you for taking the Python Quiz!")
