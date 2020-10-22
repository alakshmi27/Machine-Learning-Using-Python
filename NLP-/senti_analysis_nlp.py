import tweepy
from textblob import TextBlob
import json

api_key = 'VogMwzMHZj4WzUxkdKDm69l1r'
api_key_secret = '2N6mFvhZiEd9oUogN9XxjPrWCwQ22gigEAjS3HyLWeDSzn5tgo'
access_token = '2998610996-94JAdYBQFU3kGfJGwQuqNI93eyG7zS0GSTsS7Rs'
access_token_secret = 'WFD5kRAFkPalHUO2U5GUhNFYBzl6A6X5jBx1dstx6WyiZ'

auth = tweepy.OAuthHandler(api_key,api_key_secret)

auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

check_phrase = api.search("cricket")

for tweet in check_phrase:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    json_object= json.dumps(tweet._json)
 #   print(analysis.sentiment)
    if analysis.sentiment[0]>0:
        with open("positive.json", 'w') as jsonfile:
            jsonfile.write(json_object)
    elif analysis.sentiment[0]<0:
        with open("negative.json", 'w') as jsonfile:
            jsonfile.write(json_object)
    else:
        with open("neutral.json", 'w') as jsonfile:
            jsonfile.write(json_object)

