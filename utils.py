# utils.py
import fitz  # PyMuPDF
import json
import spacy

nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(file):
    text = ""
    with fitz.open(stream=file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text

def extract_skills(text):
    doc = nlp(text.lower())
    tokens = [token.text for token in doc if not token.is_stop and not token.is_punct]
    return set(tokens)

def load_skill_db():
    with open("skill_database.json", "r") as f:
        return json.load(f)

def match_skills(candidate_skills, required_skills):
    matched = set()
    missing = set()
    for skill in required_skills:
        if skill.lower() in candidate_skills:
            matched.add(skill)
        else:
            missing.add(skill)
    return matched, missing

def get_learning_links(skill):
    skill_encoded = skill.replace(" ", "+")
    return {
        "Coursera": f"https://www.coursera.org/search?query={skill_encoded}",
        "Udemy": f"https://www.udemy.com/courses/search/?q={skill_encoded}",
        "edX": f"https://www.edx.org/search?q={skill_encoded}",
        "YouTube": f"https://www.youtube.com/results?search_query={skill_encoded}+tutorial"
    }

def get_learning_roadmap(skill):
    roadmaps = {
        "python": [
            "Learn basic syntax, variables, and data types",
            "Practice control flow, functions, and OOP concepts",
            "Build projects like calculators, web scrapers, or data visualizers"
        ],
        "sql": [
            "Master SELECT, WHERE, JOIN, GROUP BY, HAVING",
            "Solve SQL questions on LeetCode, HackerRank",
            "Apply SQL on real datasets using tools like BigQuery"
        ],
        "html": [
            "Understand semantic tags, tables, forms, and layout structures",
            "Build a basic portfolio site using HTML",
            "Learn accessibility and responsive design"
        ],
        "react": [
            "Learn JSX, Components, Props, and State",
            "Build dynamic forms and API-integrated UIs",
            "Deploy app on Vercel or Netlify"
        ],
        "docker": [
            "Understand Docker images, containers, and Dockerfile",
            "Containerize a small app and run locally",
            "Push image to DockerHub and deploy"
        ]
    }
    return roadmaps.get(skill.lower(), [
        "Start with beginner tutorials on YouTube",
        "Build a small project",
        "Take a structured course to go deeper"
    ])