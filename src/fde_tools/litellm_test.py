import os

from litellm import completion
from dotenv import load_dotenv

load_dotenv(override=True)

tell_a_joke = [
    {"role": "user", "content": "Tell a joke for a student on the journey to becoming an expert in LLM Engineering"},
]

# response = completion(model="openai/gpt-4", messages=tell_a_joke)
# reply = response.choices[0].message.content
# print(reply)
# print(f"Input tokens: {response.usage.prompt_tokens}")
# print(f"Output tokens: {response.usage.completion_tokens}")
# print(f"Total tokens: {response.usage.total_tokens}")
# print(f"Total cost: {response._hidden_params["response_cost"]*100:.4f} cents")


response2 = completion(model="gemini/gemini-3.8-flash", messages=tell_a_joke, api_key=os.getenv("GOOGLE_API_KEY"))
reply2 = response2.choices[0].message.content
print(reply2)
print(f"Input tokens: {response2.usage.prompt_tokens}")
print(f"Output tokens: {response2.usage.completion_tokens}")
print(f"Total tokens: {response2.usage.total_tokens}")
print(f"Total cost: {response2._hidden_params["response_cost"]*100:.4f} cents")