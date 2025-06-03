from django.core.management.base import BaseCommand
from api.models import Tweet, Sentiment140Tweet
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib


class Command(BaseCommand):
    help = 'Train sentiment model using Sentiment140 and apply to collected tweets'

    def handle(self, *args, **kwargs):
        # Step 1: Load Sentiment140 data
        data = Sentiment140Tweet.objects.all().values_list('text', 'sentiment')
        texts, labels = zip(*data)

        # Normalize sentiment labels: 0=neg, 2=neutral, 4=pos → 'negative', 'neutral', 'positive'
        labels = ['negative' if l == 0 else 'neutral' if l == 2 else 'positive' for l in labels]

        # Step 2: Split and vectorize
        X_train, _, y_train, _ = train_test_split(texts, labels, test_size=0.2, random_state=42)
        vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
        X_train_vectors = vectorizer.fit_transform(X_train)

        # Step 3: Train classifier
        model = LogisticRegression(max_iter=1000)
        model.fit(X_train_vectors, y_train)

        # Step 4: Classify collected tweets
        collected = Tweet.objects.all()
        collected_texts = [t.text for t in collected]
        collected_vectors = vectorizer.transform(collected_texts)
        predictions = model.predict(collected_vectors)

        # Step 5: Update database
        for tweet, sentiment in zip(collected, predictions):
            tweet.sentiment = sentiment
            tweet.save()

        self.stdout.write(self.style.SUCCESS('Sentiment classification applied successfully to collected tweets.'))
