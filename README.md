# 🔍 LinkedIn Skill Gap Analyzer + Career Mind Map 🌱

An AI-powered **Streamlit web app** to analyze your **LinkedIn Resume** and any **Job Description**, detect the **skill gap**, and generate a personalized **learning roadmap** with XP levels, visual charts, and a downloadable PDF report.

💡 Bonus: Explore a beautifully structured **career mind map** to guide your upskilling journey!

## 🚀 Features

### 📊 Skill Gap Analyzer
- Upload your **LinkedIn Resume (PDF)**
- Paste a **Job Description**
- Get:
  - ✅ Matched & ❌ Missing Skills
  - 🎯 Skill Fit Score
  - 🧠 Learning Resources + AI Roadmap
  - 🏆 XP & 🎓 Skill Level
  - 📥 Downloadable Skill Report (PDF)

### 🌱 Career Learning Mind Map
- Choose a career role (e.g., Data Scientist, Backend Developer)
- See a **visual, expandable roadmap** of all key skills and subtopics
- Powered by D3.js and dynamic JSON



## 📦 Tech Stack

| Area         | Technology        |
|--------------|------------------|
| Frontend     | Streamlit        |
| Backend      | Python           |
| Visualization| Altair, D3.js    |
| PDF Report   | FPDF             |
| Skill Logic  | Custom AI/ML Skill Match Engine |

---

## 🚀 Local Setup Instructions

1. **Clone the Repo**
git clone https://github.com/Sandhyapyla/linkedin-skill-gap-analyzer.git
cd linkedin-skill-gap-analyzer
Create and Activate Virtual Environment

python -m venv venv
venv\Scripts\activate  # Windows
# OR
source venv/bin/activate  # Mac/Linux
Install Dependencies
pip install -r requirements.txt
Download spaCy Model
python -m spacy download en_core_web_sm

Run the App
streamlit run app.py
## 🌐 Live Deployment

🚀 My app is live at:  
**[🔗 LinkedIn Skill Gap Analyzer (Streamlit)](https://linkedin-skill-gap-analyzer-f3epvxeppqwzlvvz8cc2s3.streamlit.app/)**


📁 Project Structure

├── app.py                        # Main Streamlit app
├── utils.py                      # Skill extraction logic
├── xp_engine.py                 # XP + Level engine
├── report_generator.py          # PDF generation logic
├── components/
│   └── mindmap_component.html    # D3-based mind map renderer
├── learning_paths.json  # Nested JSON for mind map
├── requirements.txt              # Dependencies

📄 License
This project is licensed under the MIT License.
