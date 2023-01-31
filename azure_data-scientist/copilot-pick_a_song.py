# pick a random song from the artist called passenger
# using the spotify api
# and play it with mpv

import os
import requests
# get a list of all the songs
# by the artist passenger
# using the spotify api
def get_songs():
    songs = []
    # get the first 50 songs
    url = 'https://api.spotify.com/v1/artists/0X2BH1fck6amBIoJhDVmmJ/top-tracks?market=US'
    response = requests.get(url)
    response_json = response.json()
    for item in response_json['tracks']:
        songs.append(item['name'])
    return songs
    
    # no token provided. so that's fine. I should get a token. 