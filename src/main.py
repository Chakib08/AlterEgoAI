import os
from openai import OpenAI
from dotenv import load_dotenv
from typing import List

import prompts
from utils import save

def generate(images_list: List) -> str:
    # Settings
    model = "gpt-image-1"
    images = images_list
    prompt = input("Hello how can i help you today ? \n")

    # Load .env file
    load_dotenv()
    client = OpenAI(api_key=os.getenv("OPEN_API_KEY"))        
    result = client.images.edit(
        model=model,
        image=images,
        prompt=prompt
    )
        
    return result.data[0].b64_json
    

def main() -> None:

    input_img = input("Please enter you image name: ")
    images = [
        open(input_img, "rb"),
    ]
    image_base64 = generate(images)
    output_img = save(input_img, image_base64)
    print("Generated image saved {}".format(output_img))
        
main()