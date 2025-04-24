import os
from flask import Flask, request, render_template
from dotenv import load_dotenv
from openai import OpenAI

# Load the .env file and set API key
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    response = ""
    if request.method == "POST":
        try:
            user_input = request.form["user_input"]
            completion = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": user_input}
                ]
            )
            response = completion.choices[0].message.content
        except Exception as e:
            print("❌ ERROR:", e)
            response = "Sorry, something went wrong. Check the terminal."
    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)
