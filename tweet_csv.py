import os
import csv

def save_tweets_to_csv(tweets, filename, tweets_dir):
    os.makedirs(tweets_dir, exist_ok=True)
    with open(filename, mode="w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["created_at", "id", "text", "like_count", "retweet_count"])
        for tweet in tweets:
            like_count = getattr(tweet, "public_metrics", {}).get("like_count", "")
            retweet_count = getattr(tweet, "public_metrics", {}).get("retweet_count", "")
            writer.writerow([
                tweet.created_at,
                tweet.id,
                tweet.text.replace("\n", " "),
                like_count,
                retweet_count
            ])
