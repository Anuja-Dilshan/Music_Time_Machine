import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials



spotify_Client_ID= "SPOTIFY CLIENT ID"
spotify_Client_Secret= "SPOTIFY DEVELOPER CLIENT SECRET CODE"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
                                                         client_id=spotify_Client_ID,
                                                         redirect_uri="http://example.com",
                                                         client_secret=spotify_Client_Secret,
                                                         scope="playlist-modify-private"
                                                        )
)

response1 = sp.search(q="track:I'm Good (Blue)   ", type='track', limit=1)
print(response1["tracks"]["items"][0]['uri'])
