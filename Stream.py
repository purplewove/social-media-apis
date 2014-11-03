from MyStreamer import MyStreamer
    
class Stream():
    def __init__(self, app_key, app_secret, oauth_token, oauth_token_secret):
        self.streamer = MyStreamer(app_key, app_secret, oauth_token, oauth_token_secret)

    def filter_terms(self, terms):
	self.streamer.filter_terms(terms)    

