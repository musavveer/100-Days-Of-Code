import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

juice_wrld_uri = 'spotify:artist:4MCBfE4596Uoi2O4DtmEMz'
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=" ",client_secret=" "))

results = spotify.artist_albums(juice_wrld_uri, album_type='album')
albums = results['items']
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])
