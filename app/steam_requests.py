
# ****************************** steam_requests.py ******************************
# Holds all of our requests that will be sent to the steam api.
# *******************************************************************************

import requests, json
from bs4 import BeautifulSoup
from config import STEAM_API_KEY
from flask import jsonify

# Get a steam users info
def userinfo(steam_id):
    options = {
        'key': STEAM_API_KEY,
        'steamids': steam_id
    }

    url = 'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0001/?'
    rv = requests.get(url, params=options).json()
    return rv['response']['players']['player'][0] or {}

# Get a steam users wishlist
def userwishlist(steam_id):
    url = 'http://steamcommunity.com/profiles/%s/wishlist/' %steam_id
    rv = requests.get(url)
    soup=BeautifulSoup(rv.text)
    h4=soup.find_all('h4')
    setOfGames = []
    games = {}
    for i in range(len(h4)):
      games['game'] = str(h4[i]).strip('<h4></h4>')
      setOfGames.append(games['game'])
    return setOfGames

# Get a games image
def getgameimage(game_name):
    url = 'http://steamcommunity.com/app/6060'
    rv = requests.get(url)
    soup=BeautifulSoup(rv.text)
    return soup.text
