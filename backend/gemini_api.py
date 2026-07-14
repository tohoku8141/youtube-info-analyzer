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
文字数は指定しません。通常の要約としてまとめず、視聴者が動画を見終えたときに得る情報の流れが分かるように、時系列で出来事・話題・新しい知識の追加を整理してください。

新しい出来事や話題が始まるたびに区切る
重要なリアクションや状況の変化も含める
同じ内容の繰り返しはまとめる
専門用語や新しい概念は省略しない
最終的に「動画の流れ」が一目で分かるようにする

基本的に長い動画であれば要約も長くなるはずですが、雑談動画や中継など、情報の内容の変化が少ないものは要約は短くなるはずです

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
