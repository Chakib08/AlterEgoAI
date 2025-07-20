import os
from openai import OpenAI
import base64
from flask import Flask, redirect, url_for, render_template, request
from dotenv import load_dotenv
from typing import List

from utils import save

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)


def openai_generate(images: List, prompt: str) -> str:
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

@app.route('/generate', methods=['POST'])
def generate():
    user_image = request.files.get('user_image')
    character_image = request.files.get('character_image')
    prompt = request.form.get('prompt', '').strip()
    if not prompt:
        prompt = "Blend these two images into an imaginative alter ego of the person."

    saved_paths = []

    if user_image:
        user_path = os.path.join(app.config['UPLOAD_FOLDER'], user_image.filename)
        user_image.save(user_path)
        saved_paths.append(user_path)

    if character_image:
        char_path = os.path.join(app.config['UPLOAD_FOLDER'], character_image.filename)
        character_image.save(char_path)
        saved_paths.append(char_path)

    image_files = [open(path, "rb") for path in saved_paths]

    try:
        # Call openai client to generate the image
        b64_image = openai_generate(image_files, prompt)
        # Save the generated image on the same location as user image path
        output_path = save("static/alter_ego_ai.png", b64_image)
        with open(output_path, "wb") as f:
            f.write(base64.b64decode(b64_image))
        return f"/{output_path}"
    except Exception as e:
        return f"Error: {str(e)}", 500
    finally:
        for f in image_files:
            f.close()

def main() -> None:
    app.run()

if __name__ == "__main__":  
    main()