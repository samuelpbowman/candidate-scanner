import tweepy
import json
import config as config
from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd

auth = tweepy.OAuthHandler(config.api_key,config.api_secret)
auth.set_access_token(config.access_token,config.access_secret)

twitter = tweepy.API(auth)

candidates = []

with open("src/resources/dem_candidates.json","r") as candidate_file:
	candidate_data = json.load(candidate_file)
	candidates = candidate_data["candidates"]

profiles = [twitter.get_user(candidate["handle"])
        for candidate in candidates]

stats = {}
for candidate in candidates:
	timeline = twitter.user_timeline(screen_name=candidate["handle"],count=15)
	favourites = [tweet.favorite_count for tweet in timeline]
	fav_count = sum(favourites) / 15
	stats[candidate["handle"]] = fav_count

s = pd.Series(stats,name="favorites")
s.index.name = "favorites"
df = pd.DataFrame(s)
df.plot(kind='bar',color='blue')

plt.show()
