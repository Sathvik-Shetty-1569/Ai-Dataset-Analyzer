import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

def generate_code(question, columns):

    prompt = f"""
        You are a data scientist.
        
        A pandas dataframe named df is already loaded.
        
        Dataset columns:
        {columns}
        
        User question:
        {question}
        
        Rules:
        - Do NOT use import statements
        - pandas is already available as pd
        - matplotlib is already available as plt
        - Only output Python code """

    response = model.generate_content(prompt)

    return response.text