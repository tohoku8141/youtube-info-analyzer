from fastapi import FastAPI
from pydantic import BaseModel

from youtube_api import (
    get_video_info,
    get_top_comments
)

from transcript_api import get_transcript
from gemini_api import analyze_transcript
from analyzer import calculate_metrics

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173",
                   "https://youtube-info-analyzer.vercel.app/"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class VideoRequest(BaseModel):
    url: str


@app.post("/analyze")
def analyze(request: VideoRequest):

    # 動画情報取得
    info = get_video_info(request.url)

    # 字幕取得
    transcript = get_transcript(info["video_id"])

    # Gemini解析
    gemini_result = analyze_transcript(transcript)

    # 各種指標計算
    metrics = calculate_metrics(
        transcript=transcript,
        summary=gemini_result["summary"],
        duration_seconds=info["duration"],
        information_density=gemini_result["information_density"]
    )

    # コメント取得
    comments = get_top_comments(info["video_id"])

    return {
        "title": info["title"],
        "views": info["views"],
        "duration": info["duration"],

        "summary": gemini_result["summary"],

        "conciseness": metrics["conciseness"],
        "speech_speed": metrics["speech_speed"],
        "information_density": metrics["information_density"],

        "score": metrics["score"],
        "rank": metrics["rank"],

        "comments": comments
    }
