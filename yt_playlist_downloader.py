from pytube import Playlist

playlist = Playlist('https://www.youtube.com/playlist?...')

for video in playlist.video:
	print(video.title)
	video.streams.first().download()