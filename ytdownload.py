from pytube import YouTube
from sys import argv

# This will take link from command line
link = argv[1]
yt = YouTube(link)

print(f"Title: {yt.title}")
print(f"Views: {yt.views}")

yd = yt.streams.get_by_resolution("720p")

download_path = r"./path"
yd.download(download_path)
