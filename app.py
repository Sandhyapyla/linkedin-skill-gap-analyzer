import streamlit as st
import streamlit.components.v1 as components
import json
from utils import (
    extract_text_from_pdf,
    extract_skills,
    load_skill_db,
    match_skills,
    get_learning_links,
    get_learning_roadmap
)
from report_generator import generate_pdf_report
from progress_tracker import save_progress
from xp_engine import calculate_xp, get_level
import altair as alt
import pandas as pd

st.set_page_config(page_title="Skill Gap Analyzer", layout="wide")

# Sidebar navigation
page = st.sidebar.radio("📂 Select Feature", [
    "🧠 Skill Gap Analyzer",
    "🌱 Career Learning Mind Map"
])

if page == "🧠 Skill Gap Analyzer":
    st.title("📊 LinkedIn Skill Gap Analyzer")
    st.markdown("Upload your **LinkedIn Resume PDF**, paste a **Job Description**, and see where you stand — plus get personalized learning resources and XP levels!")

    user_name = st.text_input("Enter your name (for tracking):")
    uploaded_file = st.file_uploader("Upload your LinkedIn Resume (PDF)", type=["pdf"])
    job_desc = st.text_area("Paste the Job Description here")

    skill_db = load_skill_db()
    job_role = st.selectbox("Select the Job Role for Analysis", list(skill_db.keys()))

    if st.button("Analyze"):
        if uploaded_file and job_desc.strip():
            resume_text = extract_text_from_pdf(uploaded_file)
            jd_text = job_desc
            all_text = resume_text + " " + jd_text

            extracted_skills = extract_skills(all_text)
            required_skills = skill_db.get(job_role, [])

            matched, missing = match_skills(extracted_skills, required_skills)
            score = int((len(matched) / len(required_skills)) * 100) if required_skills else 0

            # XP and Level
            xp = calculate_xp(matched, missing)
            level = get_level(xp)

            st.metric("🎯 Skill Fit Score", f"{score}%")
            st.metric("🏆 XP Gained", f"{xp}")
            st.metric("🎓 Level", level)

            # Bar chart
            chart_data = pd.DataFrame({
                'Skill Status': ['Matched Skills', 'Missing Skills'],
                'Count': [len(matched), len(missing)]
            })

            bar_chart = alt.Chart(chart_data).mark_bar().encode(
                x='Skill Status',
                y='Count',
                color='Skill Status'
            ).properties(title='Skill Matching Overview')

            st.altair_chart(bar_chart, use_container_width=True)

            # Results
            st.markdown("### ✅ Matched Skills")
            st.write(", ".join(sorted(matched)) if matched else "None")

            st.markdown("### ❌ Missing Skills")
            st.write(", ".join(sorted(missing)) if missing else "None")

            if missing:
                st.markdown("### 📘 Learning Resources + Roadmap")
                for skill in sorted(missing):
                    st.markdown(f"#### 🔧 {skill.capitalize()}")
                    links = get_learning_links(skill)
                    for platform, url in links.items():
                        st.markdown(f"- [{platform}]({url})")
                    st.markdown("🧭 **Roadmap to Learn This Skill:**")
                    roadmap = get_learning_roadmap(skill)
                    for i, step in enumerate(roadmap, 1):
                        st.markdown(f"- Step {i}: {step}")
                    st.markdown("---")

            # Save progress + generate report
            if user_name:
                save_progress(user_name, job_role, score, matched, missing)
                generate_pdf_report(user_name, job_role, matched, missing, score)
                with open("skill_report.pdf", "rb") as f:
                    st.download_button("📥 Download Skill Report (PDF)", f, file_name="Skill_Report.pdf")
        else:
            st.error("Please upload a resume and paste a job description.")

elif page == "🌱 Career Learning Mind Map":
    st.markdown("## 🧠 Visual Career Learning Map")

    with open("learning_paths.json", "r") as f:
        all_paths = json.load(f)

    selected_role = st.selectbox("Choose a Role", list(all_paths.keys()))
    role_tree = all_paths[selected_role]

    def dict_to_d3(node):
        if isinstance(node, dict):
            children = []
            for k, v in node.items():
                if isinstance(v, dict) or isinstance(v, list):
                    children.append({
                        "name": k,
                        "children": dict_to_d3(v)["children"]
                    })
                else:
                    children.append({"name": v})
            return {"name": "", "children": children}
        elif isinstance(node, list):
            return {"name": "", "children": [{"name": item} for item in node]}
        else:
            return {"name": str(node)}

    d3_data = {"name": selected_role, "children": dict_to_d3(role_tree)["children"]}
    d3_json = json.dumps(d3_data)

    with open("components/mindmap_component.html", "r", encoding="utf-8") as f:
        html = f.read().replace("{{ MINDMAP_DATA }}", d3_json)

    components.html(html, height=800, scrolling=True)
