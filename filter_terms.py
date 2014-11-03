from Stream import Stream
import sys

app_key = sys.argv[1]
app_secret = sys.argv[2]
oauth_token = sys.argv[3]
oauth_token_secret = sys.argv[4]
terms = sys.argv[5:]

stream = Stream(app_key, app_secret, oauth_token, oauth_token_secret)
stream.filter_terms(terms)
