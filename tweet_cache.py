import os
from datetime import datetime, timedelta

def get_latest_tweets_file(tweets_dir, cache_window_minutes, filename_format):
    if not os.path.exists(tweets_dir):
        return None
    files = [f for f in os.listdir(tweets_dir) if f.endswith("_tweets.csv")]
    if not files:
        return None
    files.sort(reverse=True)
    now = datetime.now()
    for f in files:
        try:
            ts_str = f.split("_tweets.csv")[0]
            ts = datetime.strptime(ts_str, "%Y%m%d_%H%M%S")
            if now - ts < timedelta(minutes=cache_window_minutes):
                return os.path.join(tweets_dir, f)
        except Exception:
            continue
    return None
