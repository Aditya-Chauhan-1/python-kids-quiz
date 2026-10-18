import streamlit as st
import streamlit.components.v1 as components

# Page config
st.set_page_config(
    page_title="Python Quiz for Kids",
    page_icon="🐍",
    layout="centered"
)

# CSS injection to hide local widgets, headers, and badges
st.markdown(
    """
    <style>
    /* Hide header toolbar, footer, and status icons */
    header {visibility: hidden !important; height: 0% !important;}
    footer {visibility: hidden !important; display: none !important;}
    div[data-testid="stStatusWidget"] {display: none !important;}
    .stAppDeployButton {display: none !important;}
    
    /* Target Manage app containers */
    [data-testid="manage-app-button"],
    [class*="viewerBadge"],
    [class*="manageApp"],
    iframe[title="streamlit-badge"] {
        display: none !important;
        visibility: hidden !important;
        opacity: 0 !important;
        pointer-events: none !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Cross-Frame JavaScript injection to find and remove the Manage app element from parent DOM
components.html(
    """
    <script>
    function removeElements() {
        try {
            const doc = window.parent.document;
            
            // Query known button attributes and tags
            const targets = doc.querySelectorAll([
                '[data-testid="manage-app-button"]',
                'div[class*="viewerBadge"]',
                'div[class*="manageApp"]',
                'iframe[title="streamlit-badge"]',
                'footer'
            ].join(','));
            
            targets.forEach(el => {
                if (el) {
                    el.style.setProperty('display', 'none', 'important');
                    el.remove();
                }
            });

            // Fallback: search all fixed position elements containing 'Manage app' text
            const allElements = doc.querySelectorAll('button, div, span');
            allElements.forEach(el => {
                if (el.innerText && el.innerText.trim() === "Manage app") {
                    const container = el.closest('div[style*="fixed"]') || el;
                    container.style.setProperty('display', 'none', 'important');
                    container.remove();
                }
            });
        } catch (e) {
            // Silently pass if browser blocks cross-frame access
        }
    }

    // Run immediately and periodically
    removeElements();
    setInterval(removeElements, 150);
    </script>
    """,
    height=0,
    width=0
)

# Title & Description
st.title("🐍 Python Quiz for Kids")
st.write("Test your Python knowledge!")

st.info("Total Questions: 10 | Each Question: 1 Mark")

# Student Details
student_name = st.text_input("Student Name", placeholder="Enter your full name")

st.markdown("### 📝 Answer All Questions")

# Quiz questions list
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
        "q": "10. What will type(10.5) return?",
        "options": ["<class 'int'>", "<class 'float'>", "<class 'str'>", "<class 'number'>"],
        "answer": "<class 'float'>"
    }
]

# Quiz Form
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

# Result calculation
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
