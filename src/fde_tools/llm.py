import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(override=True)

openai = OpenAI()

content="Tell me an interesting fact."

messages = [{"role": "user", "content": content}]

response = openai.chat.completions.create(model="gpt-5-nano", messages=messages)

print("OpenAI response:")
print(response.choices[0].message.content)

gemini = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

response = gemini.chat.completions.create(
    model="gemini-3.6-flash",
    messages=messages,
)
print("Gemini response:")
print(response.choices[0].message.content)

