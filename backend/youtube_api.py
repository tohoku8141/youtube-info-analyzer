import os
import re

import isodate

from dotenv import load_dotenv
from googleapiclient.discovery import build

load_dotenv()

youtube = build(
    "youtube",
    "v3",
    developerKey=os.getenv("YOUTUBE_API_KEY")
)


def get_video_id(url: str) -> str:
    """YouTubeのURLから動画IDを取得する"""

    patterns = [
        r"youtu\.be/([^?&]+)",
        r"youtube\.com/watch\?v=([^&]+)",
        r"youtube\.com/embed/([^?&]+)",
        r"youtube\.com/shorts/([^?&]+)"
    ]

    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)

    raise ValueError("動画IDを取得できませんでした。")

def get_video_info(url: str):

    video_id = get_video_id(url)

    response = youtube.videos().list(
        part="snippet,statistics,contentDetails",
        id=video_id
    ).execute()

    if len(response["items"]) == 0:
        raise Exception("動画が見つかりません")

    item = response["items"][0]

    title = item["snippet"]["title"]

    views = int(item["statistics"]["viewCount"])

    duration = isodate.parse_duration(
        item["contentDetails"]["duration"]
    ).total_seconds()

    return {
        "video_id": video_id,
        "title": title,
        "views": views,
        "duration": duration
    }

def get_top_comments(video_id: str, max_results: int = 5):
    """
    人気コメントを取得する
    """

    response = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        order="relevance",
        maxResults=max_results,
        textFormat="plainText"
    ).execute()

    comments = []

    for item in response["items"]:

        comment = item["snippet"]["topLevelComment"]["snippet"]

        comments.append({
            "text": comment["textDisplay"],
            "likes": comment["likeCount"]
        })

    return comments
