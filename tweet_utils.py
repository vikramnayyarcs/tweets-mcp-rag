import os
import tweepy
import csv
from datetime import datetime
from tweet_cache import get_latest_tweets_file
from tweet_csv import save_tweets_to_csv

TWEETS_DIR = "tweets_data"
TWEETS_FILENAME_FORMAT = "%Y%m%d_%H%M%S_tweets.csv"
CACHE_WINDOW_MINUTES = 15

def fetch_and_cache_tweets():
    X_BEARER_TOKEN = os.getenv("X_BEARER_TOKEN")
    client = tweepy.Client(bearer_token=X_BEARER_TOKEN)
    latest_file = get_latest_tweets_file(TWEETS_DIR, CACHE_WINDOW_MINUTES, TWEETS_FILENAME_FORMAT)
    tweets = None
    if latest_file:
        print(f"Using cached tweets from {latest_file}")
        with open(latest_file, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            tweets = list(reader)
    else:
        try:
            user = client.get_user(username="VikramNayyarCS")
            user_id = user.data.id
            tweets_response = client.get_users_tweets(
                id=user_id,
                max_results=100
            )
            tweets = tweets_response.data
            if tweets:
                timestamp = datetime.now().strftime(TWEETS_FILENAME_FORMAT)
                filename = os.path.join(TWEETS_DIR, timestamp)
                save_tweets_to_csv(tweets, filename, TWEETS_DIR)
            else:
                print("No tweets found.")
                tweets = []
        except Exception as e:
            print(f"Error fetching tweets: {e}")
            tweets = []
    return tweets
