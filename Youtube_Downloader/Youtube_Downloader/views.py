from django.shortcuts import render, redirect
from pytube import YouTube

def video_downloader(request):
    if request.method == "POST":
        link = request.POST['link']
        video: YouTube = YouTube(link)

        #setting video resolution
        stream = video.streams.get_highest_resolution()

        #download video
        stream.download()

        return render(request, 'youtube.html')
    return render(request, 'youtube.html')