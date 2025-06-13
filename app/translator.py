import os
from openai import OpenAI
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

def translate_business_need_to_spec(business_prompt: str) -> str:
    """
    Translates a business need into a GenAI-based solution spec.
    """
    prompt = f"""
You are an AI business analyst assistant.

The user will give you a high-level business problem. Your job is to translate it into:
- A Business Requirements Summary
- Suggested Generative AI Use Case(s)
- Required Data
- Technical Architecture Overview
- Implementation Timeline (basic)
- Tools and Technologies (e.g., GPT-4, LangChain, Pinecone, etc.)

Business Problem:
\"\"\"{business_prompt}\"\"\"

Structured Output:
"""

    response = client.chat.completions.create(
        model="mistralai/mistral-7b-instruct:free",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4
    )

    return response.choices[0].message.content
