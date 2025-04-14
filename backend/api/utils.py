import os
import requests
from dotenv import load_dotenv
from .models import Tweet
from django.core.cache import cache
from datetime import datetime


# Load environment variables from the .env file
load_dotenv()

BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")

print("✅ Loaded Bearer:", BEARER_TOKEN[:10])  # Optionally log part of the token



def create_headers():
    return {
        "Authorization": f"Bearer {BEARER_TOKEN}",
    }

def fetch_recent_tweets(query="AI", max_results=15):
    cache_key = f"tweets_{query}"
    cached_data = cache.get(cache_key)

    url = "https://api.twitter.com/2/tweets/search/recent"
    params = {
        "query": query,
        "tweet.fields": "created_at,public_metrics,author_id",
        "expansions": "author_id",
        "user.fields": "username,verified,public_metrics",
        "max_results": max_results
    }
    headers = create_headers()
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        cache.set(cache_key, data, timeout=60)
        return data

    elif response.status_code == 429:
        print("⚠️ Twitter rate limit hit. Using cached data if available.")
        if cached_data:
            return cached_data
        else:
            return {
                "data": [],
                "includes": {"users": []},
                "meta": {"note": "Rate limit hit, no cached data available."}
            }

    else:
        print(f"❌ Twitter API error: {response.status_code} - {response.text}")
        if cached_data:
            return cached_data
        else:
            return {
                "data": [],
                "includes": {"users": []},
                "meta": {"note": "Unknown error, no cached data."}
            }


def save_tweets_to_db(data):
    tweets = data.get("data", [])
    users = {u["id"]: u for u in data.get("includes", {}).get("users", [])}

    for t in tweets:
        user = users.get(t["author_id"], {})
        metrics = t["public_metrics"]
        user_metrics = user.get("public_metrics", {})

        Tweet.objects.update_or_create(
            id=t["id"],
            defaults={
                "text": t["text"],
                "created_at": t["created_at"],
                "author_id": t["author_id"],
                "username": user.get("username", ""),
                "verified": user.get("verified", False),
                "retweet_count": metrics.get("retweet_count", 0),
                "like_count": metrics.get("like_count", 0),
                "reply_count": metrics.get("reply_count", 0),
                "quote_count": metrics.get("quote_count", 0),
                "followers_count": user_metrics.get("followers_count", 0),
                "following_count": user_metrics.get("following_count", 0),
                "tweet_count": user_metrics.get("tweet_count", 0),
                "listed_count": user_metrics.get("listed_count", 0),
                "hashtags": "",
                "mentions": "",
                "geo_location": "",
                "cleaned_text": "",
                "sentiment_score": 2,  # default neutral
            }
        )
