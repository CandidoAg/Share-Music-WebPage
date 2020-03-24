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
    categories = sorted(getDataAPI.getAllCategories(), reverse=False, key=lambda x: x['name'])
    context = {
        'categories': categories,
    }
    return render(request, 'shareMusic/Discover.html', context)


def categotyDetails(request, categoryId):
    data = getDataAPI.getPlayListByCategory(categoryId)['playlists']
    dataItems = data['items']
    playLists = []
    for playList in dataItems:
        playLists.append({'name': playList['name'], 'id': playList['id'], 'like': False})

    context = {
        'categoryName': '', #TODO put name of category
        'playLists': playLists,
    }
    return render(request, 'shareMusic/PlayListByCategory.html', context)


def songByCategoryPlayList(request, playListId):
    data = getDataAPI.getSongsByPlayList(playListId)['items']
    songs = []
    for items in data:
            artists = ""
            for artist in items['track']['artists']:
                artists += artist['name']+", "
            artists = artists[:-2]
            songs.append({'name': items['track']['name'], 'artists': artists, 'like': False})

    context = {
        'categoryName': '',  #TODO put name of playList
        'songs': songs,
    }
    return render(request, 'shareMusic/songsByCategoryList.html', context)


def perfil(request):
    context = {
        'user': 'Juan',
    }
    return render(request, 'shareMusic/Perfil.html', context)


def logout(request):
    return render(request, 'shareMusic/Logout.html')
