from youtube_api import get_video_info, get_top_comments

url = input("YouTube URL: ")

info = get_video_info(url)

comments = get_top_comments(info["video_id"])

print()
print("===== 人気コメント =====")
print()

for i, comment in enumerate(comments, start=1):

    print(f"{i}位")
    print(f"👍 {comment['likes']}")
    print(comment["text"])
    print("-" * 50)
