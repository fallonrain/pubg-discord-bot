import requests
from datetime import datetime

STEAM_PUBG_APP_ID = 578080
STEAM_NEWS_URL = (
    "https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/"
    f"?appid={STEAM_PUBG_APP_ID}&count=5&maxlength=300"
)

KEYWORDS = [
    "update",
    "maintenance",
    "patch",
    "downtime"
]


def check_pubg_update():
    try:
        response = requests.get(STEAM_NEWS_URL, timeout=5)
        response.raise_for_status()
        data = response.json()

        news_items = data.get("appnews", {}).get("newsitems", [])

        if not news_items:
            return None

        latest = news_items[0]
        title = latest.get("title", "")
        content = latest.get("contents", "")
        url = latest.get("url", "")
        timestamp = latest.get("date")

        text = f"{title} {content}".lower()

        has_update = any(keyword in text for keyword in KEYWORDS)

        date = datetime.fromtimestamp(timestamp).strftime("%d/%m/%Y %H:%M")

        return {
            "has_update": has_update,
            "title": title,
            "date": date,
            "url": url
        }

    except Exception:
        return None
