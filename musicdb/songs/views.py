from django.shortcuts import render, HttpResponse
from django.template import loader

from .models import Song

# Create your views here.
def index(request):
    song_list = Song.objects.all()
    template = loader.get_template('songs/index.html')
    context = {
            'song_list': song_list
    }
    return HttpResponse(template.render(context, request))

def detail(request, song_id):
    song = Song.objects.get(id=song_id)
    template = loader.get_template('songs/detail.html')
    context = {
            'song': song
    }
    return HttpResponse(template.render(context, request))
