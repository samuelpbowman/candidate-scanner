import tweepy
import json
import config as config

auth = tweepy.OAuthHandler(config.api_key,config.api_secret)
auth.set_access_token(config.access_token,config.access_secret)

twitter = tweepy.API(auth)

candidates = []

with open("src/resources/dem_candidates.json","r") as candidate_file:
    candidate_data = json.load(candidate_file)
    candidates = candidate_data["candidates"]

profiles = [twitter.get_user(candidate["handle"])
        for candidate in candidates]

top_tens = [twitter.user_timeline(screen_name=candidate["handle"],count=10)
        for candidate in candidates]

