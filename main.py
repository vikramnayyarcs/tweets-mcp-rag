import json

with open('tweets.json', encoding='utf-8') as f:
    data = json.load(f)
    for tweet in data.get('data', []):
        print(f"{tweet['created_at']} | {tweet['id']} | {tweet['text']}")