import os
from dotenv import load_dotenv
from tweet_utils import fetch_and_cache_tweets

load_dotenv(dotenv_path=".env.local")

if __name__ == "__main__":
    fetch_and_cache_tweets()