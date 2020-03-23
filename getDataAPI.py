import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Client data
scope = 'user-library-read'
SPOTIPY_CLIENT_ID = '78ce958ba6244e9fa36c02a68f41ebf8'
SPOTIPY_CLIENT_SECRET = '1d2bfb727ce34f2b86cda50dd978e872'
SPOTIPY_CLIENT_REDIRECT_URL = 'http://localhost:9090'

client_credentials_manager = SpotifyClientCredentials(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def getAlbumsByArtist(artist):
    results = spotify.artist_albums(artist, album_type='album')
    albums = results['items']
    while results['next']:
        results = spotify.next(results)
        albums.extend(results['items'])

    return albums


def getArtist(artistID):
    results = spotify.artist(artistID)
    return results['name']


def getMostPlayedSongs():
    results = spotify.playlist_tracks(playlist_id='37i9dQZEVXbMDoHDwVN2tF')
    return results


def getAllCategories():
    results = spotify.categories()
    return results
