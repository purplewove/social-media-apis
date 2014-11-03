from twython import TwythonStreamer
import sqlite3
import sys
import datetime

class MyStreamer(TwythonStreamer):
    '''a simple streamer that prints the text of a tweet to standard output'''
    def __init__(self, app_key, app_secret, oauth_token, oauth_token_secret):
      TwythonStreamer.__init__(self, app_key, app_secret, oauth_token, oauth_token_secret)

    def on_success(self, data):
        if 'text' in data:
            print (data['text'])

    def on_error(self, status_code, data):
        print status_code

    def filter_terms(self, terms):
	'.'.join(terms)
	self.statuses.filter(track = terms)

 
