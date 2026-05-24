import requests
from config import BOT_TOKEN, CHAT_ID


def send_telegram_alert(message, image_path):

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"

    with open(image_path, "rb") as image:

        payload = {
            "chat_id": CHAT_ID,
            "caption": message
        }

        files = {
            "photo": image
        }

        requests.post(url, data=payload, files=files)