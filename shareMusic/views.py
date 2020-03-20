from django.shortcuts import render, HttpResponseRedirect

import getDataAPI

##Valores státicos para pruebas
artista = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'


# Create your views here.
def home(request):
    artist = getDataAPI.getArtist(artista)
    albums = getDataAPI.getAlbumsByArtist(artista)
    print(albums)
    context = {
        'albums': albums,
        'artist': artist
    }
    return render(request, 'shareMusic/dashboard.html', context)

def secondPage(request):
    context = {
        'albums': 'Nadie',
        'artist': []
    }
    return render(request, 'shareMusic/dashboard.html',context)
