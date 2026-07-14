import os
import requests

RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")

URL = "https://youtube-transcript-api13.p.rapidapi.com/transcript"


def get_transcript(video_id, languages=["ja", "en"]):
    youtube_url = f"https://www.youtube.com/watch?v={video_id}"

    headers = {
        "x-rapidapi-key": RAPIDAPI_KEY,
        "x-rapidapi-host": "youtube-transcript-api13.p.rapidapi.com",
    }

    params = {
        "url": youtube_url,
        "flat_text": "false",
    }

    response = requests.get(
        URL,
        headers=headers,
        params=params,
        timeout=30,
    )

    response.raise_for_status()

    data = response.json()

    # APIから返ってきた字幕を1つの文章にする
    transcript = ""

    for item in data["transcript"]:
        transcript += item["text"] + " "

    return transcript.strip()
