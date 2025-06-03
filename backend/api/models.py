from django.db import models

class Tweet(models.Model):
    tweet_id = models.CharField(max_length=100, unique=True)
    text = models.TextField()
    sentiment = models.CharField(max_length=10, default='neutral')
    username = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    retweet_count = models.IntegerField()
    like_count = models.IntegerField()
    followers_count = models.IntegerField(default=0)
    hashtags = models.JSONField(blank=True, null=True)
    mentions = models.JSONField(blank=True, null=True)
    is_bot = models.BooleanField(null=True)  # Add this field


    def __str__(self):
        return f"{self.username}: {self.text[:50]}"


class TopicResult(models.Model):
    topic_id = models.IntegerField()
    name = models.TextField()
    count = models.IntegerField()
    keywords = models.JSONField()
    query = models.CharField(max_length=255, null=True, blank=True)
    user = models.CharField(max_length=255, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)



