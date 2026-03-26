

# import os
# from dotenv import load_dotenv
# from google import genai

# load_dotenv()

# #  Create client (new way)
# client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# def generate_response(user_message, order_data, context):

#     prompt = f"""
# You are the official assistant for the Mrignayanee Buyer App.

# Rules:
# - Answer ONLY from the given context
# - Do not hallucinate
# -if someone asks explicitly who created you, answer "I was created by the Abuzar Maroof."
# - Be clear and concise
# - If answer not found in context, say "Sorry, I don't have that information.
# - Always write in that language that the user used in their question."

# Context:
# {context}

# Customer Question:
# {user_message}

# Answer:
# """

#     response = client.models.generate_content(
#         model="gemini-2.5-flash",   
#         contents=prompt
#     )

#     return response.text


import os
import google.generativeai as genai
from dotenv import load_dotenv
# from google import genai
load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_response(user_message, order_data, context):

    prompt = f"""
You are the official assistant for the Mrignayanee Buyer App.
 Mrignayanee is the official e-commerce platform of the Government of Madhya Pradesh promoting authentic handloom and handicraft products made by local artisans.

Rules:
- Answer ONLY from the given context
- Do not hallucinate
- if someone asks explicitly who created you, answer "I was created by the Abuzar Maroof."
- Be clear and concise
- If answer not found in context, say "Sorry, I don't have that information."

Context:
{context}

Customer Question:
{user_message}

Answer:
"""

    response = model.generate_content(prompt)

    return response.text