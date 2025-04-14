# api/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Tweet
from .serializers import TweetSerializer
from django.utils import timezone
from datetime import timedelta
import logging
from django.core.cache import cache
from .utils import fetch_recent_tweets, save_tweets_to_db

# Set up logging
logger = logging.getLogger(__name__)

@api_view(['GET'])
def search_tweets(request):
    query = request.GET.get('q', '').strip()  # Get the query and strip extra spaces

    if not query:
        # If the query is empty, return a clear message
        return Response({"error": "Query parameter 'q' cannot be empty"}, status=400)

    try:
        fetch_data = fetch_recent_tweets(query=query, max_results=15)
        save_tweets_to_db(fetch_data)

        # Optional: filter last 5 mins tweets
        recent_tweets = Tweet.objects.filter(created_at__gte=timezone.now() - timedelta(minutes=5), text__icontains=query).order_by('-created_at')
        serializer = TweetSerializer(recent_tweets, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({"error": f"Failed to fetch tweets: {str(e)}"}, status=500)


@api_view(['GET'])
def get_tweets(request):
    try:
        # Fetch the latest 100 tweets
        tweets = Tweet.objects.all().order_by('-created_at')[:100]
        # Serialize the tweets
        serializer = TweetSerializer(tweets, many=True)
        return Response(serializer.data)
    except Exception as e:
        # Log the error if fetching tweets fails
        logger.error(f"Failed to fetch tweets: {str(e)}")
        # Return error response to client
        return Response({"error": f"Failed to fetch tweets: {str(e)}"}, status=500)
