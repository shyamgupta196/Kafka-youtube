import logging
import sys
import requests
import json
from config import config

def fetch_playlists(google_api_key, youtube_playlist_id):
    response = requests.get("""https://youtube.googleapis.com/youtube/v3/channels?part=snippet%2CcontentDetails&id=UCuQzKTzCj7uENwUIQGSThfQ""", params = {'key':google_api_key, 'playlistItem':youtube_playlist_id})
    # logging.debug('GOT %s', response.text)
    payload = response.text
    return payload, dir(response)

def main():
    google_api_key = config['google_api_key']
    logging.info("start")
    youtube_playlist_id = config['youtube_playlists']
    print(fetch_playlists(google_api_key, youtube_playlist_id))

if __name__ == "__main__":
    # logging.basicConfig(level=logging.DEBUG )
    sys.exit(main())