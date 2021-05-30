from pytube import YouTube

link = YouTube('https://www.youtube.com/watch?v=HbeCzCw1tT4')
title = link.title

print("Downloading: " + title)
link.streams.filter(res="1080p").first().download("C:\\Downloads")
print("Done!")
