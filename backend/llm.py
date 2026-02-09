import pandas as pd
from dotenv import load_dotenv
import os
from openai import OpenAI

# WSL2 / Linux
load_dotenv("/mnt/c/Users/Justin/Desktop/FORMATION/ML/.env")
# Access the keys as environment variables
openai_key = os.getenv("OPENAI_API_KEY")
print("Key loaded:", bool(openai_key))

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))


SYSTEM_PROMPT="""
You are an expert data assistant
Convert natural language questions into SQL queries.
Only return the sql query, nothing else

"""

def text_to_sql(question: str)-> str:
    response=client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role":"system", "content":SYSTEM_PROMPT},
            {"role":"user","content":question}
        ]
    )
    return response.choices[0].message.content
