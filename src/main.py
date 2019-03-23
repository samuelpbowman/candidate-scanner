import tweepy
import json
import config as config

auth = tweepy.OAuthHandler(config.api_key,config.api_secret)