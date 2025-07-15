import os
from dotenv import load_dotenv
from tweet_utils import fetch_and_cache_tweets

load_dotenv(dotenv_path=".env.local")

if __name__ == "__main__":
    tweets = fetch_and_cache_tweets()
    if tweets:
        # If cached, tweets is a list of dicts; if fresh, it's a list of Tweepy objects
        for tweet in tweets:
            if isinstance(tweet, dict):
                print(f"{tweet['created_at']}: {tweet['text']}")
            else:
                print(f"{tweet.created_at}: {tweet.text}")
    else:
        print("No tweets found.")