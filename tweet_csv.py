import os
import csv

def save_tweets_to_csv(tweets, filename, tweets_dir):
    os.makedirs(tweets_dir, exist_ok=True)
    if not tweets:
        return
    # Get all unique keys from all tweets
    all_keys = set()
    for tweet in tweets:
        if hasattr(tweet, 'to_dict'):
            all_keys.update(tweet.to_dict().keys())
        elif isinstance(tweet, dict):
            all_keys.update(tweet.keys())
    all_keys = sorted(all_keys)
    with open(filename, mode="w", newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=all_keys)
        writer.writeheader()
        for tweet in tweets:
            if hasattr(tweet, 'to_dict'):
                row = tweet.to_dict()
            elif isinstance(tweet, dict):
                row = tweet
            else:
                continue
            # Flatten nested dicts (e.g., public_metrics)
            flat_row = {}
            for k, v in row.items():
                if isinstance(v, dict):
                    for subk, subv in v.items():
                        flat_row[f"{k}.{subk}"] = subv
                else:
                    flat_row[k] = v
            writer.writerow(flat_row)
