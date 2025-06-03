import re

def is_bot_user(tweet):
    suspicious = 0

    # Rule 1: Username with numbers (bot-like)
    if re.search(r'\d{4,}', tweet.username):
        suspicious += 1

    # Rule 2: Low followers count
    if tweet.followers_count < 10:
        suspicious += 1

    # Rule 3: High hashtag/mention usage
    if tweet.hashtags and len(tweet.hashtags) > 5:
        suspicious += 1
    if tweet.mentions and len(tweet.mentions) > 5:
        suspicious += 1

    # Rule 4: Low engagement despite tweeting
    if tweet.retweet_count == 0 and tweet.like_count == 0:
        suspicious += 1

    # Final score
    return (suspicious >= 2)  # bot if 2+ flags
