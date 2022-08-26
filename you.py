from pytube import *

link = input('Enter a Youtube Video Link: ')
vid = YouTube(link)
# vid = YouTube('https://www.youtube.com/watch?v=i8aVz4558Z8')

# print(vid.streams)
vid_download = vid.streams.get_by_itag('18')
vid_download.download('Downloads')