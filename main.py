from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth


spotify_Client_ID= "SPOTIFY CLIENT ID"
spotify_Client_Secret= "SPOTIFY DEVELOPER CLIENT SECRET CODE"
user = 	"YOUR SPOTIFY USER ID"

user_date:str = input("To which date do you want to travel to?. Enter the date in this format yyyy-mm-dd:\n")
year = user_date.split("-")[0]


# __________________________________________BILLBOARD DATA_______________________________________________________________________
response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{user_date}")
response.raise_for_status()
data = response.text

soup = BeautifulSoup(data, "html.parser")
song_tags = soup.select(".a-truncate-ellipsis")
song_list = [song.get_text().strip("\n\t") for song in song_tags]




# ___________________________________________________SPOTIFY DATA____________________________________________________
song_uri_list = []
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
                                                         client_id=spotify_Client_ID,
                                                         redirect_uri="http://example.com",
                                                         client_secret=spotify_Client_Secret,
                                                         scope="playlist-modify-private"
                                                        )
)

for song in song_list:
    response1 = sp.search(q=f"track:{song}  ", type='track', limit=1)

    try:
        song_uri=response1["tracks"]["items"][0]['uri']
    except IndexError:
        print(f'The song {song} is not available in spotify :( ')

    else:
        song_uri_list.append(song_uri)

play_list = sp.user_playlist_create(user= user , name=f"{user_date} Billboard top 100"
                                    , public=False)


sp.playlist_add_items(playlist_id=play_list['id'], items=song_uri_list)

