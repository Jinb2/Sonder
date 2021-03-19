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
    ''' return top 5 tracks of artist

        args:
            name (string) : name of artist
        return:
            top_tracks (list) : list of tracks along with album image
    '''
    artist, image, uri = artistInfo(name)

    spotify = spotipy.Spotify(
        client_credentials_manager=SpotifyClientCredentials())
    results = spotify.artist_top_tracks(uri)
    top_tracks = []
    album_images = []

    for track in results['tracks'][:5]:
        track_name = track['name']
        top_tracks.append(track_name)
        album_image = track['album']['images'][0]['url']
        album_images.append(album_image)
    return top_tracks, album_images
