from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.models import User

##import getDataAPI

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


# def descubrimiento(request):
#     categories = sorted(getDataAPI.getAllCategories(), reverse=False, key=lambda x: x['name'])
#     context = {
#         'categories': categories,
#     }
#     return render(request, 'shareMusic/Discover.html', context)
#
#
# def categoryDetails(request, categoryId): #TODO Salen categorias a veces que no existe el id
#     categoryName,data = getDataAPI.getPlayListByCategory(categoryId)
#     dataItems = data['playlists']['items']
#     playLists = []
#     for playList in dataItems:
#         playLists.append({'name': playList['name'], 'id': playList['id'], 'like': False})
#
#     context = {
#         'categoryName': categoryName,
#         'playLists': playLists,
#     }
#     return render(request, 'shareMusic/PlayListByCategory.html', context)
#
#
# def songByCategoryPlayList(request, playListId):
#     playListName, data = getDataAPI.getSongsByPlayList(playListId)
#     items = data['items']
#     songs = []
#     for item in items:
#             artists = ""
#             for artist in item['track']['artists']:
#                 artists += artist['name']+", "
#             artists = artists[:-2]
#             songs.append({'name': item['track']['name'], 'artists': artists, 'like': False})
#
#     context = {
#         'categoryName': playListName,  #TODO put name of playList
#         'songs': songs,
#     }
#     return render(request, 'shareMusic/songsByCategoryList.html', context)


def perfil(request):
    user = User.objects.get(id=1)
    print(user)
    context = {
        'user': user
    }
    return render(request, 'shareMusic/Perfil.html', context)


def logout(request):
    return render(request, 'shareMusic/Logout.html')
