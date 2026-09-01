import os
import requests

PAGE_ID = "61592486321836"
ACCESS_TOKEN = os.getenv("FB_TOKEN")

def post_to_page(message):
    url = f"https://graph.facebook.com/v19.0/{PAGE_ID}/feed"
    payload = {
        "message": message,
        "access_token": ACCESS_TOKEN
    }
    r = requests.post(url, data=payload)
    print(r.json())

if __name__ == "__main__":
    post_to_page("Hello from my GitHub automation! 🚀")
