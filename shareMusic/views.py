from django.shortcuts import render, HttpResponseRedirect

import getDataAPI

##Valores státicos para pruebas
artista = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'


# Create your views here.
def home(request):
    songs = [{'name': 'uno', 'like': False}, {'name': 'dos', 'like': True}, {'name': 'tres', 'like': True},
             {'name': 'cuatro', 'like': False}]
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
    categories = sorted(getDataAPI.getAllCategories()['categories']['items'], reverse=False, key=lambda x: x['name'])
    context = {
        'categories': categories,
    }
    return render(request, 'shareMusic/Discover.html', context)


def categotyDetails(request, categoryId):
    data = getDataAPI.getsongsByCategory(categoryId)['playlists']
    dataItems = data['items']
    print(data)
    songs = []
    for song in dataItems:
        songs.append({'name': song['name'],'like': False})

    context = {
        'categoryName': data['name'],
        'songs': songs,
    }
    return render(request, 'shareMusic/playListByCategory.html', context)


def perfil(request):
    context = {
        'user': 'Juan',
    }
    return render(request, 'shareMusic/Perfil.html', context)


def logout(request):
    return render(request, 'shareMusic/Logout.html')
