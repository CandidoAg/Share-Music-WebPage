from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.models import User

from getDataAPI import getData

# TODO Branch User
#  change getData to use the user get in login


def login(request):
    return render(request, "shareMusic/login.html")


@login_required
def home(request):
    getData.set_user(User.objects.filter(id=request.session['_auth_user_id'])[0])
    if request.POST.get('next'):
        return HttpResponseRedirect(request.POST.get('next'))
    else:
        songs = [{'name': 'uno', 'like': False}, {'name': 'dos', 'like': True}, {'name': 'tres', 'like': True},
                 {'name': 'cuatro', 'like': False}]
        context = {
            'songs': songs,
        }
        return render(request, 'shareMusic/dashboard.html', context)

@login_required
def playlist(request):
    context = {
        'playLists': []
    }
    return render(request, 'shareMusic/Playlists.html', context)


@login_required
def descubrimiento(request):
    categories = sorted(getData.getAllCategories(), reverse=False, key=lambda x: x['name'])
    context = {
        'categories': categories,
    }
    return render(request, 'shareMusic/Discover.html', context)


@login_required
def categoryDetails(request, categoryId):  # TODO Salen categorias a veces que no existe el id
    categoryName, data = getData.getPlayListByCategory(categoryId)
    dataItems = data['playlists']['items']
    playLists = []
    for playList in dataItems:
        playLists.append({'name': playList['name'], 'id': playList['id'], 'like': False})

    context = {
        'categoryName': categoryName,
        'playLists': playLists,
    }
    return render(request, 'shareMusic/PlayListByCategory.html', context)


@login_required
def songByCategoryPlayList(request, playListId):
    playListName, data = getData.getSongsByPlayList(playListId)
    items = data['items']
    songs = []
    for item in items:
        artists = ""
        for artist in item['track']['artists']:
            artists += artist['name'] + ", "
        artists = artists[:-2]
        songs.append({'name': item['track']['name'], 'artists': artists, 'like': False})

    context = {
        'categoryName': playListName,
        'songs': songs,
    }
    return render(request, 'shareMusic/songsByCategoryList.html', context)


@login_required
def perfil(request):
    user = getData.currentUser()
    context = {
        'user': user
    }
    return render(request, 'shareMusic/Perfil.html', context)
