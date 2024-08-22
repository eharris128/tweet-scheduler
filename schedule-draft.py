from dotenv import load_dotenv
import requests
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")

def get_multiline_input(prompt="Enter content (end input Ctrl+Z and return on Windows):\n"):
    print(prompt)
    input_lines = []
    while True:
        try:
            line = input()
        except EOFError:  # Detect Ctrl+D or Ctrl+Z
            break
        input_lines.append(line)
    return "\n".join(input_lines)

def post_to_typefully(content):
    url = "https://api.typefully.com/v1/drafts/"
    payload = {
        "content": content,
        "auto_retweet_enabled": True,
        "auto_plug_enabled": True,
        "schedule-date": "next-free-slot"
    }
    headers = {
        "Content-Type": "application/json",
        "x-api-key": API_KEY
    }
    response = requests.post(url, json=payload, headers=headers)
    return response

if __name__ == "__main__":
    content = get_multiline_input()
    if content.strip():  # Ensure content is not empty
        response = post_to_typefully(content)
        print("Response Status Code:", response.status_code)
        print("Response Body:", response.json())
    else:
        print("No content provided.")
