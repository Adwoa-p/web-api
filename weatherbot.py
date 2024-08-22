import os
import json
from requests_oauthlib import OAuth1Session
from dotenv import load_dotenv
import tweepy


load_dotenv() 

CONSUMER_API_KEY=os.getenv('CONSUMER_API_KEY')
CONSUMER_API_SECRET=os.getenv('CONSUMER_API_SECRET')

APP_ACCESS_KEY=os.getenv('APP_ACCESS_KEY')
APP_ACCESS_SECRET=os.getenv('APP_ACCESS_SECRET')

client = tweepy.Client(
    consumer_key=CONSUMER_API_KEY,
    consumer_secret=CONSUMER_API_SECRET,
    access_token=APP_ACCESS_KEY,
    access_token_secret=APP_ACCESS_SECRET
)

response = client.create_tweet(text="hello world I am here again")


request_token_url = "https://api.twitter.com/oauth/request_token"
oauth = OAuth1Session(CONSUMER_API_KEY, client_secret=CONSUMER_API_SECRET)

try:
    fetch_response = oauth.fetch_request_token(request_token_url)
except ValueError:
    print(
        "There may have been an issue with the consumer_key or consumer_secret you entered."
    )

resource_owner_key = fetch_response.get("oauth_token")
resource_owner_secret = fetch_response.get("oauth_token_secret")
print("Got OAuth token: %s" % resource_owner_key)
print("Got OAuth token secret: %s" % resource_owner_secret)


# # Get authorization
base_authorization_url = "https://api.twitter.com/oauth/authorize"
authorization_url = oauth.authorization_url(base_authorization_url)
print("Please go here and authorize: %s" % authorization_url)
verifier = input("Paste the PIN here: ")

print("Got Verifier: %s" % verifier)
# # Make the request
oauth = OAuth1Session(
    CONSUMER_API_KEY,
    client_secret=CONSUMER_API_SECRET,
    resource_owner_key=resource_owner_key,
    resource_owner_secret=resource_owner_secret,
    verifier=verifier,
)
access_token_url = "https://api.twitter.com/oauth/access_token"
oauth_tokens = oauth.fetch_access_token(access_token_url)

access_token = oauth_tokens["oauth_token"]
access_token_secret = oauth_tokens["oauth_token_secret"]

# Make the request
oauth = OAuth1Session(
    CONSUMER_API_KEY,
    client_secret=CONSUMER_API_SECRET,
    resource_owner_key=access_token,
    resource_owner_secret=access_token_secret,
)


fields = "created_at,description"
params = {"user.fields": fields}

response = oauth.get("https://api.twitter.com/2/users/me", params=params)
print(response)


if response.status_code != 200:
    raise Exception(
        "Request returned an error: {} {}".format(response.status_code, response.text)
    )

print("Response code: {}".format(response.status_code))

json_response = response.json()

print(json.dumps(json_response, indent=4, sort_keys=True))

user_params={
    "username": "tbello__"
}

response_users_by_username = oauth.get(
    "https://api.twitter.com/2/users/by/username/:tbello__"
)

print(response_users_by_username)