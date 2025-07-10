import os
from openai import OpenAI
from flask import Flask, redirect, url_for, render_template, request, send_from_directory
from dotenv import load_dotenv
from typing import List
from utils import save

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)


# def generate(images: List, prompt: str) -> str:
#     # Settings
#     model = "gpt-image-1"
    
#     # Load .env file
#     load_dotenv()
#     client = OpenAI(api_key=os.getenv("OPEN_API_KEY"))        
#     result = client.images.edit(
#         model=model,
#         image=images,
#         prompt=prompt
#     )
        
#     return result.data[0].b64_json
    
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/<name>")
def user(name):
    return f"Hello {name}"

@app.route("/admin")
def admin():
    return redirect(url_for("home"))

@app.route('/generate', methods=['POST'])
def generate():
    user_image = request.files.get('user_image')
    character_image = request.files.get('character_image')
    prompt = request.form.get('prompt')

    if user_image:
        print(f"User uploaded: {user_image.filename}")
    if character_image:
        print(f"Character uploaded: {character_image.filename}")
    print(f"Prompt: {prompt}")

    # Save images (optional)
    if user_image:
        user_image.save(os.path.join(app.config['UPLOAD_FOLDER'], user_image.filename))
    if character_image:
        character_image.save(os.path.join(app.config['UPLOAD_FOLDER'], character_image.filename))

    # For now, return a static image as the result
    return '/static/soldier.png'


def main() -> None:
    app.run()


if __name__ == "__main__":  
    main()