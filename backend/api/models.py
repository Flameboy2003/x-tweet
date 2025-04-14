from django.db import models
from django.utils import timezone

class Tweet(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    text = models.TextField()
    created_at = models.DateTimeField()

    author_id = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    verified = models.BooleanField(default=False)

    retweet_count = models.IntegerField(default=0)
    like_count = models.IntegerField(default=0)
    reply_count = models.IntegerField(default=0)
    quote_count = models.IntegerField(default=0)

    followers_count = models.IntegerField(default=0)
    following_count = models.IntegerField(default=0)
    tweet_count = models.IntegerField(default=0)
    listed_count = models.IntegerField(default=0)

    hashtags = models.TextField(blank=True)
    mentions = models.TextField(blank=True)
    geo_location = models.CharField(max_length=255, default="", blank=True)

    cleaned_text = models.TextField(blank=True)
    sentiment_score = models.IntegerField(default=2)  # 0-Negative, 2-Neutral, 4-Positive

    def __str__(self):
        return self.text
