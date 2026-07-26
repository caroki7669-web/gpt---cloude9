import os, requests
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"), override=True)

PAGE_ID = os.getenv("FB_PAGE_ID")
TOKEN = os.getenv("FB_PAGE_ACCESS_TOKEN")

if not PAGE_ID or not TOKEN:
    raise RuntimeError("FB_PAGE_ID أو FB_PAGE_ACCESS_TOKEN مش متحمّلين من .env")

def post_video(video_path, description=""):
    url = f"https://graph-video.facebook.com/v20.0/{PAGE_ID}/videos"
    with open(video_path, "rb") as f:
        files = {"source": f}
        data = {"description": description, "access_token": TOKEN}
        resp = requests.post(url, files=files, data=data)
    if not resp.ok:
        print("رد فيسبوك الكامل:", resp.text)
    resp.raise_for_status()
    return resp.json()

if __name__ == "__main__":
    print(post_video("output/final.mp4", "منشور تجريبي آلي"))
