import os
import urllib.request

allfiles = [f for f in os.listdir(os.getcwd()) if os.path.isfile(os.path.join(os.getcwd(), f))] # noqa E501


for line in open('video.txt'):
    line = line.split("@")
    video_name = "{}.mp4".format(line[0])
    video_link = line[1]
    if video_name not in allfiles:
        urllib.request.urlretrieve(video_link, video_name)
        print(f"Complete: {video_name}")

print("Success")
