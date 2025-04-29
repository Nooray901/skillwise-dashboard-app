
import streamlit as st

# ------------------------------ Banner ------------------------------
st.image("https://i.ibb.co/k0PN6QV/skillwise-banner.png", use_column_width=True)

# ------------------------------
# Sample course data and metadata
# ------------------------------
courses = {
    "Python for Beginners": ["Data Analysis with Pandas", "Intro to SQL", "Python Projects"],
    "Data Analysis with Pandas": ["Data Visualization", "Intermediate Python", "Statistics 101"],
    "Intro to SQL": ["Advanced SQL", "Database Design", "SQL for Data Science"],
    "Machine Learning A-Z": ["Deep Learning Basics", "AI for Business", "Python for ML"]
}

course_metadata = {
    "Data Analysis with Pandas": {"level": "Intermediate", "domain": "Data"},
    "SQL for Data Science": {"level": "Intermediate", "domain": "Data"},
    "Python for Beginners": {"level": "Beginner", "domain": "Programming"},
    "Machine Learning A-Z": {"level": "Advanced", "domain": "AI"},
    "Intro to SQL": {"level": "Beginner", "domain": "Data"},
    "Python Projects": {"level": "Intermediate", "domain": "Programming"},
    "Data Visualization": {"level": "Intermediate", "domain": "Data"},
    "Intermediate Python": {"level": "Intermediate", "domain": "Programming"},
    "Statistics 101": {"level": "Beginner", "domain": "Data"},
    "Advanced SQL": {"level": "Advanced", "domain": "Data"},
    "Database Design": {"level": "Intermediate", "domain": "Data"},
    "Deep Learning Basics": {"level": "Advanced", "domain": "AI"},
    "AI for Business": {"level": "Advanced", "domain": "AI"},
    "Python for ML": {"level": "Advanced", "domain": "Programming"}
}

reasons = {
    "Data Analysis with Pandas": "Builds on Python foundations.",
    "SQL for Data Science": "Complements your data analysis skills.",
    "Python for Beginners": "Perfect entry point to coding.",
    "Machine Learning A-Z": "Deepens understanding of AI concepts.",
    "Intro to SQL": "Essential for understanding databases.",
    "Python Projects": "Hands-on practice to boost your skills.",
    "Data Visualization": "Great for presenting insights clearly.",
    "Intermediate Python": "Takes your coding to the next level.",
    "Statistics 101": "Builds essential math for data science."
}

# ------------------------------
# App UI
# ------------------------------
st.markdown("<h1 style='text-align: center; color: green;'>SkillWise: Personalized Learning Dashboard</h1>", unsafe_allow_html=True)
st.caption("Your progress. Your pace. Smart course recommendations, reimagined.")

# ------------------------------
# Sidebar filters
# ------------------------------
st.sidebar.header("🎛️ Filter Recommendations")
selected_level = st.sidebar.selectbox("Select Level", ["All", "Beginner", "Intermediate", "Advanced"])
selected_domain = st.sidebar.selectbox("Select Domain", ["All", "Data", "Programming", "AI"])

# ------------------------------
# User course selection
# ------------------------------
st.markdown("### 🎯 Recommended for You")
selected_course = st.selectbox("Select a course you've completed:", list(courses.keys()))
recommended_courses = courses.get(selected_course, [])

def filter_courses(course_list):
    filtered = []
    for course in course_list:
        meta = course_metadata.get(course, {})
        if (selected_level == "All" or meta.get("level") == selected_level) and            (selected_domain == "All" or meta.get("domain") == selected_domain):
            filtered.append(course)
    return filtered

filtered_courses = filter_courses(recommended_courses)

# ------------------------------
# Show Recommendations
# ------------------------------
cols = st.columns(4)
for i, course in enumerate(filtered_courses):
    with cols[i % 4]:
        st.markdown(f"💻 **{course}**")
        st.markdown(f"Level: **{course_metadata[course]['level']}**")
        st.caption(f"💡 _Why? {reasons.get(course, '')}_")
        st.button("View Details", key=f"view_{course}")

# ------------------------------
# Skill Progress
# ------------------------------
st.markdown("---")
st.subheader("📊 Your Skill Progress")
st.progress(0.6, text="Python - 60%")
st.progress(0.3, text="Data Analysis - 30%")
st.progress(0.8, text="AI Readiness - 80%")
