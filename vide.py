# from pytube import YouTube


# from pytube import YouTube

# link = "https://youtu.be/OKuiyX5k6zg?si=ybV5eTnldmFJtS2_"
# youtube_1 = YouTube(link)

# # print(youtube_1.title)
# # print(youtube_1.thumbnail_url)

# # videos=youtube_1.streams.all() (all format list)
# # videos=youtube_1.streams.filter(only_audio=True) #only audion

# vid=list(enumerate(videos))
# for i in vid:
#     print(i)

# strm=int(input("enter : "))

# videos[strm].download()
# print('successfully')

#    playlist #

from pytube import Playlist

playlist_url = "https://youtu.be/FOGRHBp6lvM?si=zuvCnDvPvyB9RwrB"
py = Playlist(playlist_url)

try:
    print(f'Downloading: {py.title}')
except KeyError:
    # Handle the case where the 'list' key is not present in the query
    print("Unable to retrieve playlist information. Please check the URL.")

for video in py.videos:
    video.streams.first().download()
