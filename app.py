import streamlit as st
from db import init_db, add_user, login
from resume_parser import extract_text
from generate_pdf import generate_report
from career_suggestions import suggest_careers
import os
from groq import Groq

# Initialize DB
init_db()

# Page config
st.set_page_config(
    page_title="🌟 Pathfinder's Future Finder",
    page_icon="✨",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for soft colors
st.markdown("""
<style>
body {
    background-color: #FFF8F0;
    color: #444;
}
.stButton>button {
    background-color: #FF9999;
    color: white;
    border-radius: 10px;
    padding: 10px;
    font-size: 16px;
}
.stTextInput > div > div > input {
    background-color: #FFE0D5;
    border: 1px solid #FFB3A1;
}
</style>
""", unsafe_allow_html=True)

# Cute footer
st.markdown("<p style='text-align:center; color:#FF9999;'>Made with 💖 by vaishnavi sinha </p>", unsafe_allow_html=True)

# Session state for login
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'user_name' not in st.session_state:
    st.session_state.user_name = ""
if 'suggestions' not in st.session_state:
    st.session_state.suggestions = None
if 'pookie_message' not in st.session_state:
    st.session_state.pookie_message = None
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Login/Signup Page
if not st.session_state.logged_in:
    st.title("🌟 Pathfinder's Future Finder")
    st.write("Log in or sign up to upload your resume!")

    choice = st.radio("Choose:", ["Login", "Sign Up"])

    if choice == "Login":
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            if login(email, password):
                st.session_state.logged_in = True
                st.session_state.user_name = email.split('@')[0].title()
                st.success("Logged in successfully! 🎉")
                st.rerun()
            else:
                st.error("Invalid credentials ❌")

    else:
        name = st.text_input("Your Name")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        if st.button("Sign Up"):
            if add_user(name, email, password):
                st.success("Account created! You can now log in. ✅")
            else:
                st.error("Email already exists 😔")

# Dashboard (after login)
else:
    st.title(f"✨ Welcome, {st.session_state.user_name}! 🌸")
    st.subheader("Upload your resume to discover your top 3 career paths! 🚀")

    uploaded_file = st.file_uploader("Choose your resume (PDF or DOCX)", type=["pdf", "docx"])

    if uploaded_file is not None:
        try:
            with st.spinner("📄 Parsing your resume and consulting ..."):

                # Save uploaded file
                temp_path = "temp_resume.pdf"
                with open(temp_path, "wb") as f:
                    f.write(uploaded_file.getvalue())

                # Extract text
                text = extract_text(temp_path)

                # Initialize Groq client
                client = Groq(api_key=st.secrets["GROQ_API_KEY"])

                # 🌟 1. Pookie's Personal Message (only once)
                if st.session_state.pookie_message is None:
                    message_prompt = f"""
                    You're Pathfinder's Future Finder, a sweet, proud AI fairy godmother. 
                    Talk to {st.session_state.user_name}, who just uploaded their resume. 
                    Be warm, encouraging, and a little funny. Use emojis. Exactly 3 short sentences.
                    """
                    msg_response = client.chat.completions.create(
                        messages=[{"role": "user", "content": message_prompt}],
                        model="llama-3.1-8b-instant",
                        max_tokens=120,
                        temperature=0.9,
                    )
                    st.session_state.pookie_message = msg_response.choices[0].message.content.strip()

                # Display Pookie's note
                st.markdown("###  🌟 Pathfinder's Future Finder Says:")
                st.markdown(f"> {st.session_state.pookie_message}")
                st.snow()  # ✨ Light snow effect
                st.markdown("---")

                # 🎯 2. Career Suggestions (only once)
                if st.session_state.suggestions is None:
                    career_prompt = f"""
                    You're 🌟 Pathfinder's Future Finder, a fun career advisor. Based on this resume, suggest exactly 3 dream career paths.

                    For each:
                    1. Job title
                    2. Why it's a great fit (1 sentence)
                    3. One actionable tip

                    Use emojis and keep it encouraging! Max 200 words.

                    Resume: {text[:4000]}
                    """
                    career_response = client.chat.completions.create(
                        messages=[{"role": "user", "content": career_prompt}],
                        model="llama-3.1-8b-instant",
                        max_tokens=500,
                        temperature=0.7,
                    )
                    st.session_state.suggestions = career_response.choices[0].message.content.strip()

                # Show suggestions
                st.write("### 🎯 Your Top 3 Career Matches:")
                st.write(st.session_state.suggestions)

                # 📄 PDF Generation
                if st.button("📥 Generate Career Report PDF"):
                    pdf_filename = f"{st.session_state.user_name}_career_report.pdf"
                    generate_report(st.session_state.user_name, st.session_state.suggestions, pdf_filename)

                    with open(pdf_filename, "rb") as f:
                        st.download_button(
                            "⬇️ Download Your Career Report",
                            f,
                            file_name=pdf_filename,
                            mime="application/pdf"
                        )

                    st.balloons()
                    st.markdown(
                        f"<h3 style='text-align:center; color:#FF9999;'>You've got this, {st.session_state.user_name}! 💕</h3>",
                        unsafe_allow_html=True
                    )

                # 💬 Bonus: Ask Pookie for Advice
                st.markdown("---")
                if st.button("💬 Ask 🌟 Pathfinder's Future Finder for Advice"):
                    advice_prompt = f"""
                    You're 🌟 Pathfinder's Future Finder, the cutest AI fairy. {st.session_state.user_name} wants one piece of career advice.
                    Give one short, uplifting tip. Use emojis. 1 sentence only!
                    """
                    advice_response = client.chat.completions.create(
                        messages=[{"role": "user", "content": advice_prompt}],
                        model="llama-3.1-8b-instant",
                        max_tokens=60,
                        temperature=0.9,
                    )
                    advice = advice_response.choices[0].message.content.strip()
                    st.info(advice)

        except Exception as e:
            st.error("Oops! Something went wrong while processing your resume.")
            st.exception(e)
        finally:
            # Clean up temp file
            if os.path.exists("temp_resume.pdf"):
                os.remove("temp_resume.pdf")

    # --- Always show at bottom (logged in only) ---

    # Logout button
    if st.button("🚪 Logout"):
        st.session_state.clear()
        st.rerun()

    # Motivational footer
    st.markdown("---")
    st.markdown("### 🌸 Keep Shining!")
    st.markdown(
        f"You're one step closer to your dream career, {st.session_state.user_name}. "
        "🌟 Pathfinder's Future Finder believes in you! 💖"
    )

    # 💬 Pookie Chatbot in Sidebar
    with st.sidebar:
        st.markdown("### 💬 Chat with 🌟 Pathfinder's Future Finder")
        st.markdown("Ask career advice, life tips, or just say hi! 💌")

        # Initialize chat history if needed
        if "chat_history" not in st.session_state:
            st.session_state.chat_history = [
                {"role": "assistant", "content": f"Hi {st.session_state.user_name}! I'm  💖 What's on your mind?"}
            ]

        # Display chat
        for msg in st.session_state.chat_history:
            icon = "🧚‍♀️" if msg["role"] == "assistant" else "👤"
            with st.chat_message(msg["role"], avatar=icon):
                st.write(msg["content"])

        # Input
        if prompt := st.chat_input("Ask 🌟 Pathfinder's Future Finder..."):
            st.session_state.chat_history.append({"role": "user", "content": prompt})

            # Send to LLM
            client = Groq(api_key=st.secrets["GROQ_API_KEY"])
            response = client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": "You are 🌟 Pathfinder's Future Finder, a warm, funny, encouraging AI fairy godmother. Respond in 1–2 short sentences. Use emojis. Be kind and proud."
                    }
                ] + st.session_state.chat_history,
                model="llama-3.1-8b-instant",
                max_tokens=150,
                temperature=0.9,
            )

            reply = response.choices[0].message.content.strip()
            st.session_state.chat_history.append({"role": "assistant", "content": reply})
            st.rerun()