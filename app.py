from flask import Flask, render_template, request
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

app = Flask(__name__)

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
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"

@app.route("/", methods=["GET", "POST"])
def home():
    processed = ""
    answer = ""
    if request.method == "POST":
        user_question = request.form.get("question", "")
        processed = preprocess(user_question)
        answer = query_or(processed)
    return render_template("index.html", processed=processed, answer=answer)

if __name__ == "__main__":
    app.run(debug=True)
