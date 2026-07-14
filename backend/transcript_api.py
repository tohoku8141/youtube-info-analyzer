from youtube_transcript_api import YouTubeTranscriptApi


def get_transcript(video_id: str, languages=["ja", "en"]):
    """
    字幕を取得して1つの文字列にまとめる
    """

    transcript = YouTubeTranscriptApi().fetch(
        video_id,
        languages=languages
    )

    text = ""

    for item in transcript:
        text += item.text + " "

    return text.strip()
