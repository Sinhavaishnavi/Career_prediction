Career_Finder
An AI-Powered Career Recommendation System

Career_Finder is a desktop application designed to assist students and recent graduates in navigating their career paths. The system analyzes a user's resume to extract key skills and experiences, leveraging this data to provide personalized, data-driven career recommendations. Its intuitive user interface simplifies the process of career exploration, providing a practical tool for career guidance.
Key Features

    Secure Authentication: User login and registration are managed through a lightweight SQLite database.

    Resume Parsing: Supports text extraction from common resume formats, including PDF and DOCX files.

    Intelligent Recommendations: Provides the top three most relevant career paths based on parsed resume content.

    Custom Reporting: Generates a downloadable, professional PDF report summarizing the user's profile and recommendations.

    Intuitive User Experience: The application is built on a clean and encouraging user interface designed for ease of use.

    Scalable Architecture: The system's design is ready for future integration with advanced Large Language Models (LLMs) to enhance recommendation accuracy and depth.
<img width="1634" height="756" alt="image" src="https://github.com/user-attachments/assets/b6680486-6c8c-4a3f-b733-197b1249731f" />
<img width="1534" height="769" alt="image" src="https://github.com/user-attachments/assets/1845450f-c656-4bc9-9f7d-a9dcdb06520d" />
<img width="1866" height="824" alt="image" src="https://github.com/user-attachments/assets/c76b9d9a-a32a-4277-a353-b341347ad49f" />
<img width="1768" height="774" alt="image" src="https://github.com/user-attachments/assets/4e37fc7e-ccb8-4fa6-be18-661b5fd99533" />



Tech Stack

The application is built primarily on Python, utilizing the following libraries and technologies:

    Frontend: Streamlit

    Backend: Python

    Database: SQLite

    Parsing: PyPDF2, python-docx

    PDF Generation: FPDF2

    LLM Integration: OpenAI API

Installation and Setup

To run this application locally, follow these steps:

    Clone the repository:

    git clone https://github.com/Sinhavaishnavi/career_prediction.git
    cd career_prediction

    Create and activate a virtual environment:

    python -m venv venv
    # On macOS/Linux
    source venv/bin/activate
    # On Windows
    venv\Scripts\activate

    Install dependencies:

    pip install -r requirements.txt

    Launch the application:

    streamlit run app.py



    Note: For the full functionality, ensure your OpenAI API key is configured in secrets.toml or as an environment variable.

Project Structure

pookies-future-finder/
├── app.py                  # Main Streamlit application entry point
├── db.py                   # Handles database initialization and user authentication logic
├── resume_parser.py        # Contains functions for parsing resume files
├── career_suggestions.py   # Core logic for generating career recommendations
├── generate_pdf.py         # Manages the generation of PDF career reports
├── requirements.txt        # Lists all required Python packages
└── README.md               # Project overview and documentation

Roadmap & Future Development

    LLM Integration: Implement deeper resume analysis and conversational features using advanced LLMs.

    Skill Gap Analysis: Introduce a feature to identify skill deficiencies and suggest relevant learning resources.

    Deployment: Prepare the application for a production environment with a more robust database system like PostgreSQL or Firebase.

    Internationalization: Expand language support to cater to a broader, global user base.

Contributing

Contributions are welcome! Please feel free to report bugs, suggest new features, or submit pull requests. For more detailed information, please refer to the CONTRIBUTING.md file.

    Fork the project.

    Create your feature branch: git checkout -b feature/your-new-feature

    Commit your changes: git commit -m 'feat: Describe your feature'

    Push to the branch: git push origin feature/your-new-feature

    Open a pull request.

License

This project is licensed under the MIT License. See the LICENSE file for more details.
Contact

For inquiries, please connect with the project author, Vaishnavi, on LinkedIn.
