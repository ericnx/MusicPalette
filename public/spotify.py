import spotipy
import requests
from pprint import pprint
import os
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")

scopes = "user-read-playback-state, user-read-currently-playing, app-remote-control, streaming, playlist-read-private"

sp_oauth = spotipy.SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET, redirect_uri=REDIRECT_URI, scope=scopes)
token = sp_oauth.get_cached_token()
access_token = token["access_token"]

sp = spotipy.Spotify(auth=access_token)

current_song = sp.current_user_playing_track()
pprint(current_song)