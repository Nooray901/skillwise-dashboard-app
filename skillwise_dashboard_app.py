
import streamlit as st
from PIL import Image

st.set_page_config(page_title="SkillWise Dashboard", layout="wide")

# Header
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>SkillWise: Personalized Learning Dashboard</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Your progress. Your pace. Smart course recommendations, reimagined.</p>", unsafe_allow_html=True)
st.markdown("---")

# Recommended Courses Grid
st.subheader("🎯 Recommended for You")

cols = st.columns(4)

course_info = [
    {"title": "Data Analysis with Pandas", "level": "Intermediate"},
    {"title": "SQL for Data Science", "level": "Intermediate"},
    {"title": "Python for Beginners", "level": "Beginner"},
    {"title": "Machine Learning A-Z", "level": "Advanced"}
]

for col, course in zip(cols, course_info):
    with col:
        st.image("https://static.thenounproject.com/png/3574486-200.png", width=60)
        st.markdown(f"**{course['title']}**")
        st.caption(f"Level: {course['level']}")
        st.button("View Details", key=course['title'])

st.markdown("---")

# Skill Progress Section
st.subheader("📈 Your Skill Progress")
st.progress(45)
st.caption("You’ve completed 3 out of 7 modules. Keep going!")

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center;'>🚀 Future-ready learning platform, powered by AI.</p>", unsafe_allow_html=True)
