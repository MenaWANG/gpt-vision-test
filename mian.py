import base64
import requests
from mimetypes import guess_type

# get openai_api_key
# ---- config approach
from config import openai_api_key
api_key = openai_api_key
# ---- env variable approach
# import os
# api_key = os.environ.get("OPENAI_API_KEY")

# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

# Function to encode a local image into data URL 
def local_image_to_data_url(image_path):
    # Guess the MIME type of the image based on the file extension
    mime_type, _ = guess_type(image_path)
    if mime_type is None:
        mime_type = 'application/octet-stream'  # Default MIME type if none is found

    # Read and encode the image file
    base64_encoded_data = encode_image(image_path)

    # Construct the data URL
    return f"data:{mime_type};base64,{base64_encoded_data}"

# Path to your image
image_path = "images/dummy-receipt1.png"

# Getting the data path
data_url = local_image_to_data_url(image_path)

headers = {
  "Content-Type": "application/json",
  "Authorization": f"Bearer {api_key}"
}

payload = {
  "model": "gpt-4-turbo",
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "What’s in this image?"
        },
        {
          "type": "image_url",
          "image_url": {
            "url": data_url
          }
        }
      ]
    }
  ],
  "max_tokens": 300
}

response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

print(response.json())