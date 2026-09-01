import os, requests
token = os.getenv("FB_TOKEN")
page_id = "61592486321836"
url = f"https://graph.facebook.com/{page_id}/feed"
msg = "Hello from my GitHub automation! 🚀"
r = requests.post(url, data={"message": msg, "access_token": token})
print(r.text)
