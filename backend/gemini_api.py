import os
import json

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def analyze_transcript(transcript: str):

    prompt = f"""
あなたはYouTube動画を分析するAIです。

以下の字幕を解析してください。

やることは2つだけです。

① 動画全体を要約してください。
・文字数は指定しません。
・必要最小限の文字数で、重要な情報を漏らさず要約してください。

② この動画の情報密度を100点満点で評価してください。

評価基準
・新しい知識
・具体性
・論理性
・有益性
・重複の少なさ

必ずJSONのみを出力してください。

{{
    "summary": "...",
    "information_density": 85
}}

字幕

=======================

{transcript}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    text = response.text.strip()

    # ```json ～ ``` を除去
    if text.startswith("```"):
        text = text.split("\n", 1)[1]
        text = text.rsplit("```", 1)[0]

    return json.loads(text)
