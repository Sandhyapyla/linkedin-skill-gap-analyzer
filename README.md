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

## 🛠️ Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/YOUR_USERNAME/linkedin-skill-gap-analyzer.git
cd linkedin-skill-gap-analyzer
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Run the Streamlit app

bash
Copy
Edit
streamlit run app.py
View in your browser at
http://localhost:8501

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
