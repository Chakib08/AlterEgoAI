import os
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv

import prompts


def main() -> None:
    
    # Settings
    model = "gpt-3.5-turbo"
    temperature = 0.3
    max_tokens = 500
    
    # Contents
    system_message = prompts.system_message
    prompt = input("Hello i'm CultureGPT, ask me any question related to general culture \n")
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
        # Example call
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens
        )

        print(response.choices[0].message.content)
        print("\n")
        new_prompt = input()
        messages[1]["content"] = new_prompt
        

main()
