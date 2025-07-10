import os
from openai import OpenAI
from flask import Flask, redirect, url_for, render_template
from dotenv import load_dotenv
from typing import List

from utils import save

app = Flask(__name__)


def generate(images: List, prompt: str) -> str:
    # Settings
    model = "gpt-image-1"
    
    # Load .env file
    load_dotenv()
    client = OpenAI(api_key=os.getenv("OPEN_API_KEY"))        
    result = client.images.edit(
        model=model,
        image=images,
        prompt=prompt
    )
        
    return result.data[0].b64_json
    
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/<name>")
def user(name):
    return f"Hello {name}"

@app.route("/admin")
def admin():
    return redirect(url_for("home"))


def main() -> None:
    app.run()


if __name__ == "__main__":  
    main()