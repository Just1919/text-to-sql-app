import streamlit as st
import requests

st.set_page_config(page_title="Text-to-SQL App", layout="centered")
st.title("Text-to-SQL Generator")
st.write("Convert natural language questions into SQL queries using AI")

# Lien vers ton backend FastAPI local (changera après déploiement)
API_URL = "http://127.0.0.1:8000/generate-sql"

question = st.text_area("Enter your question:")

if st.button("Generate SQL"):
    if question.strip():
        try:
            response = requests.post(API_URL, json={"question": question})
            if response.status_code == 200:
                sql = response.json()["sql"]
                st.code(sql, language="sql")
            else:
                st.error(f"Error {response.status_code}: {response.text}")
        except Exception as e:
            st.error(f"API request failed: {e}")
    else:
        st.warning("Please enter a question")
