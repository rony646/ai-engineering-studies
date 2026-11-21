from openai import OpenAI
from dotenv import load_dotenv

import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)

results = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system", "content": "You are a math teacher"
        },
        {
            "role": "user", "content": "Tell me about your job"
        }
    ]
)

print(results.choices[0].message.content)