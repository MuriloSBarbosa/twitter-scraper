import pandas as pd
import json

def format_medias(medias) -> list:
    if not medias:
        return []
    urls = []
    for media in medias:
        if media['type'] == 'video' and 'video_info' in media:
            for variant in media['video_info']['variants']:
                urls.append(variant['url'])
        elif 'media_url_https' in media:
            urls.append(media['media_url_https'])
    return urls

def format_tweets(tweets) -> list:
    tweets_to_store = []
    for tweet in tweets:
        tweets_to_store.append({
            'id': tweet.id,
            'created_at': tweet.created_at,
            'user': tweet.user.screen_name,
            'favorite_count': tweet.favorite_count,
            'retweet_count': tweet.retweet_count,
            'urls': tweet.urls,
            'full_text': tweet.full_text,
            'hashtags': tweet.hashtags,
            'media': format_medias(tweet.media)
        })
    df = pd.DataFrame(tweets_to_store)
    result = df.to_json(orient='records')
    return json.loads(result) 