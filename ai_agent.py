import os
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")

def ask_ai(question, dataset_info):

    prompt = f"""
    You are a data scientist.

    Dataset info:
    {dataset_info}

    User question:
    {question}

    Answer clearly.
    """

    response = model.generate_content(prompt)

    return response.text