from openai import OpenAI
import os
import re
from dotenv import load_dotenv

load_dotenv()

OR_API_KEY = os.getenv("OR_API_KEY")
MODEL = os.getenv("OR_MODEL", "x-ai/grok-4.1-fast")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OR_API_KEY
)

def preprocess(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    return text.strip()

def query_or(question):
    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": question}],
            extra_body={"reasoning": {"enabled": True}}
        )
        answer = response.choices[0].message.content
        return answer
    except Exception as e:
        return f"Error: {e}"

def main():
    print("\n=== OpenRouter Q&A CLI ===")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("Enter your question (or 'exit'): ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        processed = preprocess(user_input)
        print(f"\nProcessed Question: {processed}")

        answer = query_or(processed)
        print(f"\nAnswer: {answer}\n")

if __name__ == "__main__":
    main()
