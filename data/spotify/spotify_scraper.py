import os
import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials

# set our id and client secret
os.environ['SPOTIPY_CLIENT_ID'] = '155d2e3110c84dd9a0e56feba36f0660'
os.environ['SPOTIPY_CLIENT_SECRET'] = '58babadbaaca47f3a951306257cab51b'


def artistInfo(name):
    ''' Get the image, uri and name of the artist

        args:
            name(string) : string of artist name
        return:
            artist's name
            artist's image uri
            artists uri id
    '''
    # create authentaction for ClientCredentials
    spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials())

    results = spotify.search(q='artist:' + name, type='artist')
    items = results['artists']['items']
    if len(items) > 0:
        artist = items[0]
    return artist['name'], artist['images'][0]['url'], artist['uri']


def getTopTracks(name):
    # create authentaction for ClientCredentials
    spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials())

    artist, image, uri = artistInfo(name)

    results = spotify.artist_top_tracks(uri)
    for track in results['tracks'][:10]:
        print('track    : ' + track['name'])
        print('audio    : ' + track['preview_url'])
        print('cover art: ' + track['album']['images'][0]['url'])
        print()
