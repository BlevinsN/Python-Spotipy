#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 09:52:09 2020

@author: blev
"""


import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util

cid = "CID"
secret = "SECRET"
username = "USERNAME"

client_credentials_manager = SpotifyClientCredentials(client_id = cid, client_secret = secret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

scope = 'user-library-read playlist-read-private'
token = util.prompt_for_user_token(username, scope)

if token:
    sp = spotipy.Spotify(auth=token)
else:
    print("Can't get token for", username)
