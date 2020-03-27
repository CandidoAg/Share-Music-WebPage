import spotipy
from django.conf import settings
from spotipy.oauth2 import SpotifyClientCredentials


class getData(object):
    user = ''
    client_credentials_manager = SpotifyClientCredentials(settings.SOCIAL_AUTH_SPOTIFY_KEY,
                                                          settings.SOCIAL_AUTH_SPOTIFY_SECRET)
    spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    class Meta:
        abstract = True


    @classmethod
    def set_user(self, username):
        self.user = username

    @classmethod
    def getAlbumsByArtist(self, artist):
        results = self.spotify.artist_albums(artist, album_type='album')
        albums = results['items']
        while results['next']:
            results = self.spotify.next(results)
            albums.extend(results['items'])

        return albums

    @classmethod
    def getArtist(self, artistID):
        results = self.spotify.artist(artistID)
        return results['name']

    @classmethod
    def getMostPlayedSongs(self):
        results = self.spotify.playlist_tracks(playlist_id='37i9dQZEVXbMDoHDwVN2tF')
        return results

    @classmethod
    def getAllCategories(self):
        results = self.spotify.categories(limit=50)['categories']['items']
        return results

    @classmethod
    def getPlayListByCategory(self, categoryId):
        results = self.spotify.category_playlists(categoryId)
        categories = self.spotify.categories(limit=50)['categories']['items']
        categoryName = ""
        for category in categories:
            if (category['id'].upper() == categoryId.upper()):
                categoryName = category['name']
        return categoryName, results

    @classmethod
    def getSongsByPlayList(self, playListId):
        results = self.spotify.playlist_tracks(playListId)
        playList = self.spotify.playlist(playListId)

        return playList['name'], results

    @classmethod
    def currentUser(self):
        print(self.user)
        results = self.spotify.user(self.user.__str__())
        return results
