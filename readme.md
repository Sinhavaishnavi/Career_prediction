
---

```markdown
# 🌟 Pookie's Future Finder

✨ Your AI-Powered Career Compass ✨  
A smart, student-friendly career recommendation app that analyzes your resume and suggests personalized career paths — all wrapped in a cute, encouraging interface.



Built with love (and code) to help students like you discover where they shine brightest.

---

## 🚀 Demo
Try the live app: COMMING SOON

![App Screenshot]() <!-- Add a screenshot if available -->

---

## 🎯 Features

- 🔐 User Login & Signup – Secure authentication with SQLite
- 📄 Resume Upload – Supports PDF and DOCX files
- 🔍 Smart Parsing – Extracts text and key details from resumes
- 💼 Career Suggestions – Recommends top 3 career matches based on content
- 📄 PDF Report Generation – Download a personalized career report
- 🎈 Fun & Encouraging UX – Designed to uplift and inspire
- 🚪 Logout & Session Management** – Clean user flow
- 🧠 LLM-Ready Architecture – Built to integrate GPT or other LLMs for smarter insights

---

## 🛠️ Tech Stack

- Frontend: [Streamlit](https://streamlit.io) (Python)
- Backend: Python scripts for parsing, logic, and PDF generation
- Database: SQLite (lightweight, file-based)
- Parsing: `PyPDF2`, `python-docx` (for text extraction)
- PDF Generation: `FPDF2` or `reportlab`
- Authentication: Custom user management
- Future: OpenAI GPT / LLM integration for intelligent career guidance

---

## 📦 Installation & Setup

1. Clone the repo:
   ```bash
   git clone https://github.com/Sinhavaishnavi/career_prediction.git
   
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the app:
   ```bash
   streamlit run app.py
   ```

5. Open your browser at `http://localhost:8501`

> 💡 Make sure to add your OpenAI API key (if using LLM) in `secrets.toml` or as an environment variable.

---

## 🗂️ Project Structure

```
pookies-future-finder/
│
├── app.py                 # Main Streamlit app
├── db.py                  # User authentication & database setup
├── resume_parser.py       # Extracts text & fields from resumes
├── career_suggestions.py  # Logic to suggest careers
├── generate_pdf.py        # Creates downloadable PDF report
├── requirements.txt       # Python dependencies
└── README.md              # You are here!
```

---

## 🌱 Future Roadmap

- ✅ Integrate **LLMs (GPT, Llama, etc.)** for deeper resume analysis
- 💬 Add a **Pookie Chatbot** – Ask career questions in real time
- 🌐 Deploy with enhanced security (e.g., Firebase or PostgreSQL)
- 🌍 Support multiple languages
- 📊 Add skill gap analysis & learning path recommendations

---

## 💖 Inspiration

This project was built for students who feel lost in the maze of career choices. Named after my inner cheerleader "Pookie", it’s more than an app — it’s a hug in digital form. 🤗

Special shoutout to every student who dares to dream big. *You've got this.*

---

## 🙌 Contributing

Contributions are welcome! Whether it's improving parsing accuracy, designing better UI, or adding LLM features — feel free to open an issue or submit a PR.

1. Fork the project
2. Create your feature branch: `git checkout -b feature/AmazingFeature`
3. Commit your changes: `git commit -m 'Add some amazing feature'`
4. Push to the branch: `git push origin feature/AmazingFeature`
5. Open a pull request

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---

## 💌 Connect With Me

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/9211)


Made with 💖 by **Vaishnavi**  🌸



