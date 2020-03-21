from django.shortcuts import render, HttpResponseRedirect

##import getDataAPI

##Valores státicos para pruebas
artista = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'


# Create your views here.
def home(request):
    songs = [{'name': 'uno'}, {'name': 'dos'}, {'name': 'tres'}, {'name': 'cuatro'}]
    context = {
        'songs': songs,
    }
    return render(request, 'shareMusic/dashboard.html', context)


def playlist(request):
    context = {
        'playLists': []
    }
    return render(request, 'shareMusic/Playlists.html', context)


def descubrimiento(request):
    context = {
        'genreList': [],
        'songsList': []
    }
    return render(request, 'shareMusic/Discover.html', context)


def perfil(request):
    context = {
        'user': 'Juan',
    }
    return render(request, 'shareMusic/Perfil.html', context)


def logout(request):
    return render(request, 'shareMusic/Logout.html')
