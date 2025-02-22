from pprint import pprint
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
from flask import Flask, redirect, request, url_for
import spotipy
import os

app = Flask(__name__)
load_dotenv()
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")

scopes = "user-read-playback-state, user-read-currently-playing, app-remote-control, streaming, playlist-read-private"
# authorize the user to get access token
sp_oauth = SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET, redirect_uri=REDIRECT_URI, scope=scopes)    
token = sp_oauth.get_access_token()
access_token = token["access_token"]

@app.route("/")
def login():
    print(sp_oauth.get_cached_token())    
    return redirect(url_for("current_song", ac_token=access_token))

# @app.route("/callback")
# def callback():
#     code = request.args.get("code")
#     cached_token = sp_oauth.get_access_token(code)
#     return redirect("/current_song")

@app.route("/current_song")
def current_song():
    access_token = request.args.get("ac_token")
    # use access token to the current song
    sp = spotipy.Spotify(auth=access_token)
    current_song = sp.current_user_playing_track()

    if current_song:
        # get the song id
        song_id = current_song["item"]["id"]
        # get the song name
        song_name = current_song["item"]["name"]
        # get the song's artists
        artists = ", ".join([artist["name"] for artist in current_song["item"]["artists"]])
        # get the song cover
        song_cover = current_song["item"]["album"]["images"][1]["url"]

        current_song_info = {
            "id": song_id,
            "name": song_name,
            "artists": artists,
            "images": song_cover
        }
        return current_song_info
    else:
        return "No song is currently playing.\n"

if __name__ == "__main__":
    app.run(debug=True, port=3000)