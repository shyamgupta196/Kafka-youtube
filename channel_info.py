import logging
import sys
import requests
import json
from config import config

def fetch_info(google_api_key):
    response = requests.get("""https://youtube.googleapis.com/youtube/v3/channels?part=snippet%2CcontentDetails&id=UCuQzKTzCj7uENwUIQGSThfQ""", params = {'key':google_api_key})
    # logging.debug('GOT %s', response.text)
    payload = response.text
    return payload, dir(response)

def main():
    google_api_key = config['google_api_key']
    logging.info("start")
    print(fetch_info(google_api_key))

if __name__ == "__main__":
    # logging.basicConfig(level=logging.DEBUG )
    sys.exit(main())