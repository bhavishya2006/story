from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
billboard_url = "https://www.billboard.com/charts/hot-100/" + date
response = requests.get(url=billboard_url, headers=header)

soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]

print("\nTop 100 Songs Retrieved:")
for index, song in enumerate(song_names, start=1):
    print(f"{index}. {song}")

CLIENT_ID = "7a06f915ebec4c4a9f26d5ae87cdad5e"
CLIENT_SECRET = "c8ee748739884d74b6dfdfc4a3e6af14"
REDIRECT_URI = "http://127.0.0.1:8888/callback"


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=REDIRECT_URI,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]
print(user_id)

song_uris = []
year = date.split("-")[0]

for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track", limit=1)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
        print(f"Found and added: {song}")
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
    time.sleep(0.5)

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

if song_uris:
    sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
    print("\nAll found songs successfully added to your playlist!")
else:
    print("No songs were added to the playlist.")
