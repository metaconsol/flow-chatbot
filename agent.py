# import os
# # import google.generativeai as genai
# from dotenv import load_dotenv
# from google import genai
# load_dotenv()

# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# model = genai.GenerativeModel("gemini-2.5-flash")


# def generate_response(user_message, order_data, context):

#     prompt = f"""
# You are the official assistant for the Mrignayanee Buyer App.

# Rules:
# - Answer ONLY from the given context
# - Do not hallucinate
# - Be clear and concise
# - If answer not found in context, say "Sorry, I don't have that information."

# Context:
# {context}

# Customer Question:
# {user_message}

# Answer:
# """

#     response = model.generate_content(prompt)

#     return response.text

import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

# ✅ Create client (new way)
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_response(user_message, order_data, context):

    prompt = f"""
You are the official assistant for the Mrignayanee Buyer App.

Rules:
- Answer ONLY from the given context
- Do not hallucinate
- Be clear and concise
- If answer not found in context, say "Sorry, I don't have that information."

Context:
{context}

Customer Question:
{user_message}

Answer:
"""

    # ✅ New API call
    response = client.models.generate_content(
        model="gemini-2.5-flash",   # or gemini-2.5-flash if enabled
        contents=prompt
    )

    return response.text