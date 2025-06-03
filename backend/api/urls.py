from django.urls import path
from . import views 
from .views import GetTweetsView
from django.urls import path 
from .views import AnomalyDetectionAPIView

urlpatterns = [
    path('search_tweets/', views.search_tweets, name='search_tweets'),#Home page Api call
    path('tweets/', GetTweetsView.as_view(), name='get_tweets'), #Tweets Page Api call 

    path('get-tweets-with-sentiment/', views.TweetSentimentView.as_view(), name='get_tweets_with_sentiment'), #sentiment page Api call

    path('anomalies/', AnomalyDetectionAPIView.as_view(), name='anomaly-detection'),

    path('influencer-impact/', views.influencer_impact, name='influencer-impact'),
    path("detect-bots/",views.BotDetectionView.as_view(), name="detect-bots"),

    path('topics/', views.get_topics, name='get_topics'),
    path('download-csv/', views.download_tweets_csv, name='download-csv'),

]
