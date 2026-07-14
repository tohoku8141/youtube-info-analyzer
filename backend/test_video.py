from youtube_api import get_video_info

url = input("YouTube URL: ")

info = get_video_info(url)

print()

print("タイトル")
print(info["title"])

print()

print("再生数")
print(f'{info["views"]:,}')

print()

print("動画時間")
print(info["duration"], "秒")

print()

print("動画ID")
print(info["video_id"])
