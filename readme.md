
---

# Career\_Finder

**An AI-Powered Career Recommendation System**
🔗 [Live Demo](https://sinhavaishnavi-prediction-app-9wve2q.streamlit.app/)

Career\_Finder is an intelligent desktop application designed to guide students and fresh graduates in exploring career opportunities. By analyzing resumes, it extracts key skills and experiences, then provides **personalized, data-driven career recommendations**. With a clean UI and scalable backend, Career\_Finder offers a reliable and practical solution for career planning.

---

## 🚀 Key Features

* **🔐 Secure Authentication** – User login & registration powered by a lightweight SQLite database.
* **📄 Resume Parsing** – Extracts content from PDF and DOCX resumes using *PyPDF2* and *python-docx*.
* **🤖 Smart Recommendations** – Suggests the top three career paths most aligned with the candidate’s profile.
* **📑 Custom Reporting** – Generates a downloadable **professional PDF report** summarizing skills & career advice.
* **🎨 Intuitive UI** – Built with Streamlit for a smooth and interactive user experience.
* **📈 Scalable Design** – Future-ready for LLM integration to provide conversational and deeper insights.

---

## 🖼️ Screenshots

<img width="1634" height="756" src="https://github.com/user-attachments/assets/b6680486-6c8c-4a3f-b733-197b1249731f"/>  
<img width="1534" height="769" src="https://github.com/user-attachments/assets/1845450f-c656-4bc9-9f7d-a9dcdb06520d"/>  
<img width="1866" height="824" src="https://github.com/user-attachments/assets/c76b9d9a-a32a-4277-a353-b341347ad49f"/>  
<img width="1768" height="774" src="https://github.com/user-attachments/assets/4e37fc7e-ccb8-4fa6-be18-661b5fd99533"/>  

---

## 🛠 Tech Stack

* **Frontend:** Streamlit
* **Backend:** Python
* **Database:** SQLite
* **Resume Parsing:** PyPDF2, python-docx
* **PDF Reports:** FPDF2
* **AI Integration:** OpenAI API

---

## ⚙️ Installation & Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/Sinhavaishnavi/career_prediction.git
   cd career_prediction
   ```
2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   # macOS/Linux
   source venv/bin/activate
   # Windows
   venv\Scripts\activate
   ```
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:

   ```bash
   streamlit run app.py
   ```
5. **Note:** Configure your OpenAI API key in `secrets.toml` or as an environment variable.

---

## 📂 Project Structure

```
career_prediction/
├── app.py                  # Streamlit app entry point
├── db.py                   # User authentication & database logic
├── resume_parser.py        # Resume parsing utilities
├── career_suggestions.py   # Core recommendation engine
├── generate_pdf.py         # PDF report generator
├── requirements.txt        # Dependencies
└── README.md               # Documentation
```

---

## 🔮 Roadmap

* **LLM Integration** – Add deeper resume analysis & conversational career coaching.
* **Skill Gap Analysis** – Identify missing skills & suggest learning resources.
* **Deployment Upgrade** – Move to PostgreSQL/Firebase for production scalability.
* **Internationalization** – Multi-language support for global accessibility.

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repo
2. Create a feature branch:

   ```bash
   git checkout -b feature/your-feature
   ```
3. Commit your changes:

   ```bash
   git commit -m 'feat: Add your feature'
   ```
4. Push and open a pull request 🚀

---

## 📜 License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---

## 📬 Contact

👩‍💻 **Author:** Vaishnavi Sinha
🔗 [LinkedIn](https://www.linkedin.com/in/vaishnavi-sinha-952111259)
📧 [vaishnavisinha476@gmail.com](mailto:vaishnavisinha476@gmail.com)

---
