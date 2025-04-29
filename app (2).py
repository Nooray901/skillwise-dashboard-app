
import streamlit as st

# ----------------- Course Data -----------------
course_data = {
    "Data Analysis with Pandas": {
        "level": "Intermediate",
        "details": "Covers data wrangling, data frames, and exploratory data analysis using the pandas library."
    },
    "SQL for Data Science": {
        "level": "Intermediate",
        "details": "Learn how to extract and analyze data using SQL queries and databases."
    },
    "Python for Beginners": {
        "level": "Beginner",
        "details": "An introduction to Python basics, variables, loops, and simple coding exercises."
    },
    "Machine Learning A-Z": {
        "level": "Advanced",
        "details": "Covers classification, regression, clustering, and model evaluation with real-world datasets."
    }
}

# ----------------- Header -----------------
st.markdown("<h1 style='text-align: center; color: green;'>SkillWise: Personalized Learning Dashboard</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Your progress. Your pace. Smart course recommendations, reimagined.</p>", unsafe_allow_html=True)
st.markdown("---")

# ----------------- Recommendation Section -----------------
st.markdown("### 🎯 Recommended for You")

cols = st.columns(4)
for i, (course, info) in enumerate(course_data.items()):
    with cols[i]:
        st.markdown("#### 💻 " + course)
        st.markdown(f"Level: **{info['level']}**")
        if st.button("View Details", key=course):
            st.session_state["selected_course"] = course

# ----------------- Course Details -----------------
if "selected_course" in st.session_state:
    course = st.session_state["selected_course"]
    st.markdown("---")
    st.markdown(f"### 📝 Course Details: {course}")
    st.success(course_data[course]["details"])

# ----------------- Skill Progress Placeholder -----------------
st.markdown("---")
st.markdown("### 📈 Your Skill Progress")
st.info("Skill progress visualization will appear here in future updates.")
