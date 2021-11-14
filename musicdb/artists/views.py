from django.shortcuts import render, HttpResponse
from django.template import loader

from .models import Artist

# Create your views here.
def index(request):
    artist_list = Artist.objects.all()
    template = loader.get_template('artists/index.html')
    context = {
            'artist_list': artist_list
    }
    return HttpResponse(template.render(context, request))

def detail(request, artist_id):
    artist = Artist.objects.get(id=artist_id)
    template = loader.get_template('artists/detail.html')
    context = {
            'artist': artist
    }
    return HttpResponse(template.render(context, request))
