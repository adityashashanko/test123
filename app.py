import streamlit as st
from openai import OpenAI
import os

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="Smart Knowledge Assistant", layout="centered")

st.title("🤖 Smart Knowledge Assistant")

# ---------------- SESSION STATE ----------------
if "question" not in st.session_state:
    st.session_state.question = ""
if "answer" not in st.session_state:
    st.session_state.answer = ""

# ---------------- INPUT ----------------
question = st.text_area(
    "Ask anything (e.g., SAP T-code, concept, topic):",
    key="question",
    height=150
)

# ---------------- BUTTONS ----------------
col1, col2, col3 = st.columns(3)

# -------- BRIEF --------
with col1:
    if st.button("Brief"):
        if question.strip():
            prompt = f"Give a very brief explanation in simple terms: {question}"

            response = client.chat.completions.create(
                model="gpt-4o-mini",
                temperature=0,
                messages=[{"role": "user", "content": prompt}]
            )

            st.session_state.answer = response.choices[0].message.content
        else:
            st.warning("Please enter a question")

# -------- DETAILED --------
with col2:
    if st.button("Detailed"):
        if question.strip():
            prompt = f"Explain in detail with examples and clarity: {question}"

            response = client.chat.completions.create(
                model="gpt-4o-mini",
                temperature=0,
                messages=[{"role": "user", "content": prompt}]
            )

            st.session_state.answer = response.choices[0].message.content
        else:
            st.warning("Please enter a question")

# -------- USE CASE --------
with col3:
    if st.button("Use Case"):
        if question.strip():
            prompt = f"Explain real-world use cases or business applications of: {question}"

            response = client.chat.completions.create(
                model="gpt-4o-mini",
                temperature=0,
                messages=[{"role": "user", "content": prompt}]
            )

            st.session_state.answer = response.choices[0].message.content
        else:
            st.warning("Please enter a question")

# -------- RESET BUTTON --------
if st.button("Reset"):
    st.session_state.clear()
    st.rerun()

# ---------------- OUTPUT ----------------
if st.session_state.answer:
    st.markdown("### 📌 Result")
    st.success(st.session_state.answer)
