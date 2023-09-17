from pytube import YouTube
url = input('url:')
yt = YouTube(url) #ссылка на видео.s
print(yt)
stream = yt.streams.get_highest_resolution()
print('dowload')
stream.download('./downloads')
# def d(c):
#     print('ama')
#     print(c)
# a = 4 
# d(a)