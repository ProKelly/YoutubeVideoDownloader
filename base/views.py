from django.shortcuts import render,redirect
from django.http import HttpResponse
from pytube import YouTube
from .forms import DonwloadForm

def home(request):
    if request.method == 'POST':
        form = DonwloadForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            try:
                yt = YouTube(url)
                stream = yt.streams.get_highest_resolution()
                response = HttpResponse(content_type='video/mp4')
                response['Content-Disposition'] = f'attachment; filename="{yt.title}.mp4"'
                stream.stream_to_buffer(response)
                return response
            except Exception as e:
                return render(request, 'base/index.html', {'form':form, 'error':'Failed to download video'})
    else:
        form = DonwloadForm()
    return render(request, 'base/index.html', {'form':form})