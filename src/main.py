import os
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
import requests
import base64


import prompts
from image2text import encode, decode


def download_image(url: str, filename: str = "output.png"):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)
        print(f"✅ Image saved as: {filename}")
    else:
        print(f"❌ Failed to download image: {response.status_code}")

def main() -> None:
    # Settings
    model = "gpt-image-1"
    temperature = 0.3
    max_tokens = 500
    
    # Contents
    system_message = prompts.system_message
    prompt = input("Hello generate image \n")
    
    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": prompt}
    ]

    # Load .env file
    load_dotenv()
    
    client = OpenAI(
        api_key=os.getenv("OPEN_API_KEY")
    )

    # Get the API key
    api_key = os.getenv("OPENAI_API_KEY")
    
    while True:
        # Text model example
        # response = client.chat.completions.create(
        #     model=model,
        #     messages=messages,
        #     temperature=temperature,
        #     max_tokens=max_tokens
        # )
        
        
        # print(response.choices[0].message.content)
        # print("\n")
        # new_prompt = input()
        # messages[1]["content"] = new_prompt
        

        
        # Image generation example
        # response = client.images.generate(
        #     model=model,
        #     prompt=prompt,
        #     n=1,
        #     size="1024x1024"
        # )
        
        # image_url = response.data[0].url
        # print(f"✅ Image generated:\n{image_url}")
        
        # print("Downloading image...")
        # download_image(image_url, "out.png")

        # print("\n")
        # new_prompt = input()
        # messages[1]["content"] = new_prompt
        
        input_img = input("Please enter you image name without extension: ")
        
        result = client.images.edit(
        model="gpt-image-1",
        image=[
            open(input_img + ".png", "rb"),
            open("layton" + ".png", "rb"),
        ],
        prompt=prompt
        )
        
        image_base64 = result.data[0].b64_json
        image_bytes = base64.b64decode(image_base64)

        # Save the image to a file
        with open(input_img + "-out.png", "wb") as f:
            f.write(image_bytes)

        print("\n")
        new_prompt = input()
        messages[1]["content"] = new_prompt
        
main()
