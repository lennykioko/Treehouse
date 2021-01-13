import urllib.request

video_link = "https://videos.teamtreehouse.com/videos/TH-WS-TypeScript-Fix-720p.mp4?token=6000809a_184edf0711c2e0a98283a72a0c9288b7d76a7393"

video_name = "41-getting-started-with-typescript-2--01-Getting Started with TypeScript.mp4"

urllib.request.urlretrieve(video_link, video_name)

print("Complete")
