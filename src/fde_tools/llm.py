from .llm_client import call_llm

content = "Tell me an interesting fact."

messages = [{"role": "user", "content": content}]

print("OpenAI response:")
response = call_llm(provider="openai", model="gpt-4-mini", messages=messages)
print(response)

print("\nGemini response:")
response = call_llm(provider="gemini", model="gemini-3.6-flash", messages=messages)
print(response)

