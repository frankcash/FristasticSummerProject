
# ****************************** youtube_requests.py *****************************
# Holds all of our requests that will be sent to the youtube api.
# *******************************************************************************

import requests, json, logging
from config import YOUTUBE_API_KEY
logging.basicConfig(filename='output.log',level=logging.WARNING)

# Get a list of videoIds pertaining to the game being searched
def search_videos(game):
    params = {
        'key': YOUTUBE_API_KEY,
        'part': 'snippet',
        'maxResults': 3,
        'order': 'relevance',
        'q': 'steam video game' + game.name,
        'type': 'video',
        'videoEmbeddable': True
    }

    url = 'https://www.googleapis.com/youtube/v3/search'
    rv = requests.get(url, params=params).json()

    videoIds = []
    if(rv['pageInfo']['totalResults'] != 0):
    	for video in rv['items']:
    		videoIds.append(video['id']['videoId'])

    return videoIds
