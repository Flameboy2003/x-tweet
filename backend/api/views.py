from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Tweet
from .serializers import TweetSerializer
import tweepy
from django.conf import settings
from rest_framework.views import APIView
from rest_framework import status
from django.http import JsonResponse
from django.views import View 

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

import re

import math
from django.db.models import Sum, Avg, F, FloatField

from django.db.models import Count
from .models import Tweet
from datetime import timedelta
from django.utils import timezone
import pandas as pd

from rest_framework.views import APIView
from rest_framework import status
import numpy as np

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_pandas.io import read_frame
from api.models import Tweet, TopicResult
from bertopic import BERTopic
from datetime import datetime

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Tweet
from .utils.bot_detection import is_bot_user

from django.http import HttpResponse
import csv
import io

@api_view(['GET'])
def search_tweets(request):
    query = request.GET.get('q')
    if not query:
        return Response({'error': 'Query parameter "q" is required.'}, status=400)

    # Initialize Tweepy client
    client = tweepy.Client(
        bearer_token=settings.TWITTER_BEARER_TOKEN
    )

    tweets_data = []
    next_token = None

    while len(tweets_data) < 10:
        response = client.search_recent_tweets(
            query=query,
            tweet_fields=['created_at', 'public_metrics'],
            expansions=['author_id'],
            user_fields=['username', 'public_metrics'],
            max_results=min(10 - len(tweets_data), 10),
            next_token=next_token
        )

        if not response.data:
            break

        # Map author_id to user details
        users = {user.id: user for user in response.includes['users']} if response.includes and 'users' in response.includes else {}

        analyzer = SentimentIntensityAnalyzer()

        for tweet in response.data:
            tweet_id = tweet.id
            text = tweet.text
            created_at = tweet.created_at
            retweet_count = tweet.public_metrics.get('retweet_count', 0)
            like_count = tweet.public_metrics.get('like_count', 0)

            user = users.get(tweet.author_id)
            username = user.username if user else 'Unknown'
            followers_count = user.public_metrics.get('followers_count', 0) if user and user.public_metrics else 0

            hashtags = re.findall(r"#(\w+)", text)
            mentions = re.findall(r"@(\w+)", text)

            sentiment_score = analyzer.polarity_scores(text)
            compound_score = sentiment_score['compound']
            if compound_score >= 0.05:
                sentiment = 'positive'
            elif compound_score <= -0.05:
                sentiment = 'negative'
            else:
                sentiment = 'neutral'

            tweet_obj, created = Tweet.objects.get_or_create(
                tweet_id=tweet_id,
                defaults={
                    'text': text,
                    'username': username,
                    'created_at': created_at,
                    'retweet_count': retweet_count,
                    'like_count': like_count,
                    'followers_count': followers_count,
                    'hashtags': hashtags,
                    'mentions': mentions,
                    'sentiment': sentiment
                }
            )
            tweets_data.append(tweet_obj)

        next_token = response.meta.get('next_token')
        if not next_token:
            break

    serializer = TweetSerializer(tweets_data, many=True)
    return Response(serializer.data)

class GetTweetsView(APIView):
    def get(self, request):
        # Retrieve all tweets from the database
        tweets = Tweet.objects.all()
        serializer = TweetSerializer(tweets, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class TweetSentimentView(View):
    def get(self, request, *args, **kwargs):
        # Fetch all tweets with their sentiment labels
        tweets = Tweet.objects.all()
        
        # Format the tweets and their sentiment in the response
        tweet_data = [
            {
                "text": tweet.text,
                "sentiment": tweet.sentiment  # Ensure your Tweet model has a 'sentiment' field
            }
            for tweet in tweets
        ]
        
        return JsonResponse(tweet_data, safe=False)
    
class AnomalyDetectionAPIView(APIView):
    """
    API view to detect anomalies using all stored tweets for a given query.
    """

    def get(self, request):
        query = request.query_params.get('query')
        if not query:
            return Response({"error": "Query parameter is required."}, status=status.HTTP_400_BAD_REQUEST)

        # Fetch all tweets matching the query (case insensitive search)
        tweets = Tweet.objects.filter(text__icontains=query).order_by('-created_at')
        if not tweets.exists():
            return Response({"error": "No tweets found for the given query."}, status=status.HTTP_404_NOT_FOUND)

        # Convert sentiment labels to numerical scores
        sentiment_scores = []
        for tweet in tweets:
            if tweet.sentiment == 'positive':
                sentiment_scores.append(1)
            elif tweet.sentiment == 'neutral':
                sentiment_scores.append(0)
            elif tweet.sentiment == 'negative':
                sentiment_scores.append(-1)

        sentiment_scores = np.array(sentiment_scores)
        mean = np.mean(sentiment_scores)
        std = np.std(sentiment_scores)

        # Define anomaly threshold as a user-defined multiplier of standard deviations
        threshold_multiplier = float(request.query_params.get('threshold', 2))
        lower_threshold = mean - threshold_multiplier * std
        upper_threshold = mean + threshold_multiplier * std

        anomalies = []
        for tweet, score in zip(tweets, sentiment_scores):
            if score < lower_threshold or score > upper_threshold:
                anomalies.append({
                    "id": tweet.id,
                    "text": tweet.text,
                    "sentiment_score": score,
                    "created_at": tweet.created_at,
                    "retweet_count": tweet.retweet_count,
                    "like_count": tweet.like_count,
                    "followers_count": tweet.followers_count,
                })

        return Response({
            "query": query,
            "anomaly_count": len(anomalies),
            "anomalies": anomalies,
            "mean_sentiment": mean,
            "std_sentiment": std,
            "thresholds": {
                "lower": lower_threshold,
                "upper": upper_threshold
            }
        })

@api_view(['GET'])
def influencer_impact(request):
    sentiment = request.GET.get('sentiment')
    min_followers = request.GET.get('min_followers')
    hashtag = request.GET.get('hashtag')

    tweets = Tweet.objects.all()

    if sentiment:
        tweets = tweets.filter(sentiment=sentiment)
    if min_followers:
        tweets = tweets.filter(followers_count__gte=int(min_followers))
    if hashtag:
        tweets = tweets.filter(hashtags__icontains=hashtag)

    influencers = (
        tweets.values('username', 'followers_count')
        .annotate(
            total_likes=Sum('like_count'),
            total_retweets=Sum('retweet_count'),
            tweet_count=Sum(1),
        )
    )

    influencer_scores = []
    for user in influencers:
        followers = user['followers_count']
        likes = user['total_likes']
        retweets = user['total_retweets']

        score = (retweets * 2 + likes) * math.log(followers + 1)
        influencer_scores.append({
            'username': user['username'],
            'followers_count': followers,
            'total_likes': likes,
            'total_retweets': retweets,
            'influence_score': round(score, 2)
        })

    influencer_scores.sort(key=lambda x: x['influence_score'], reverse=True)
    return Response(influencer_scores[:10])

    # Aggregate metrics per user
    influencers = (
        Tweet.objects
        .values('username', 'followers_count')
        .annotate(
            total_likes=Sum('like_count'),
            total_retweets=Sum('retweet_count'),
            tweet_count=Sum(1),
        )
    )

    influencer_scores = []
    for user in influencers:
        followers = user['followers_count']
        likes = user['total_likes']
        retweets = user['total_retweets']

        score = (retweets * 2 + likes) * math.log(followers + 1)
        influencer_scores.append({
            'username': user['username'],
            'followers_count': followers,
            'total_likes': likes,
            'total_retweets': retweets,
            'influence_score': round(score, 2)
        })

    # Sort and return top 10 influencers
    influencer_scores.sort(key=lambda x: x['influence_score'], reverse=True)
    return Response(influencer_scores[:10])

class BotDetectionView(APIView):
    def post(self, request):
        tweet_ids = request.data.get("tweet_ids", [])
        results = []

        tweets = Tweet.objects.filter(id__in=tweet_ids)
        for tweet in tweets:
            is_bot = is_bot_user(tweet)
            results.append({
                "tweet_id": tweet.tweet_id,
                "username": tweet.username,
                "is_bot": is_bot
            })

        return Response(results, status=status.HTTP_200_OK)


def download_tweets_csv(request):
    buffer = io.StringIO()
    writer = csv.writer(buffer)
    
    writer.writerow([
        'tweet_id', 'text', 'sentiment', 'username', 'created_at',
        'retweet_count', 'like_count', 'followers_count',
        'hashtags', 'mentions', 'is_bot'
    ])

    for tweet in Tweet.objects.all():
        writer.writerow([
            tweet.tweet_id,
            tweet.text,
            tweet.sentiment,
            tweet.username,
            tweet.created_at,
            tweet.retweet_count,
            tweet.like_count,
            tweet.followers_count,
            tweet.hashtags,
            tweet.mentions,
            tweet.is_bot
        ])

    response = HttpResponse(buffer.getvalue(), content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="tweets.csv"'
    return response

@api_view(['GET'])
def get_topics(request):
    query = request.GET.get('query')
    user = request.GET.get('user')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    # Check cache
    cached = TopicResult.objects.filter(query=query, user=user, start_date=start_date, end_date=end_date).order_by('-created_at').first()
    if cached:
        return Response({
            "topics": [{
                "topic_id": cached.topic_id,
                "name": cached.name,
                "count": cached.count,
                "keywords": cached.keywords
            }]
        })

    tweets = Tweet.objects.all()
    if query:
        tweets = tweets.filter(text__icontains=query)
    if user:
        tweets = tweets.filter(username=user)
    if start_date and end_date:
        tweets = tweets.filter(created_at__range=[start_date, end_date])

    df = read_frame(tweets[:500])  # limit to 500
    texts = df['text'].dropna().tolist()

    if not texts:
        return Response({'error': 'No tweets found'}, status=400)

    topic_model = BERTopic()
    topics, _ = topic_model.fit_transform(texts)

    topic_info = topic_model.get_topic_info().to_dict(orient='records')
    topic_words = topic_model.get_topics()

    results = []
    for topic in topic_info:
        words = [{"text": w, "weight": float(wt)} for w, wt in topic_words.get(topic["Topic"], [])]
        TopicResult.objects.create(
            topic_id=topic["Topic"],
            name=topic["Name"],
            count=topic["Count"],
            keywords=words,
            query=query,
            user=user,
            start_date=start_date if start_date else None,
            end_date=end_date if end_date else None
        )
        results.append({
            "topic_id": topic["Topic"],
            "name": topic["Name"],
            "count": topic["Count"],
            "keywords": words
        })

    return Response({"topics": results})