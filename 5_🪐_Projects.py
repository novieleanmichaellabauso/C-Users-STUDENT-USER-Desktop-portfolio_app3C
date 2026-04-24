import streamlit as st
st.title(" My Projects")

st.title("📁 My Projects Showcase")

st.write("Here are some of the projects I've worked on:")

projects = {
    "📊 E-Attendance Navigator": {
        "description": "A smart attendance system with automated reports and tracking.",
        "tech": "Python, Streamlit, SQLite"
    },
    "🌐 SAOD Web App": {
        "description": "A web platform designed to promote and support local products.",
        "tech": "HTML, CSS, JavaScript"
    },
    "🏦 Banking System": {
        "description": "A system that manages financial transactions and provides analytics.",
        "tech": "Python, MySQL"
    }
}

for name, details in projects.items():
    with st.expander(name):
        st.write(f"**Description:** {details['description']}")
        st.write(f"**Technologies Used:** {details['tech']}")

st.write("---")
st.caption("🚀 Built with Streamlit")