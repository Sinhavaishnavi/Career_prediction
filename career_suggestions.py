from groq import Groq
import streamlit as st

def suggest_careers(resume_text):
    try:
        client = Groq(api_key=st.secrets["GROQ_API_KEY"])  # Save key in Streamlit secrets

        prompt = f"""
        You're Pookie, a fun and caring career advisor. Based on this resume, suggest exactly 3 dream career paths.

        For each:
        - Job title
        - Why it's a great fit (1 sentence)
        - One actionable tip to get started

        Keep it encouraging and use emojis 💖

        Resume: {resume_text[:4000]}  # Limit length
        """

        response = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama3-8b-8192",  # or "llama3-70b-8192" for smarter answers
            max_tokens=500,
            temperature=0.7,
        )

        raw_output = response.choices[0].message.content.strip()
        return raw_output

    except Exception as e:
        return f"Error: {str(e)}"