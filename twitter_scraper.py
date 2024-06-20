from twikit import Client
from typing import Literal
from twikit import Tweet
from twikit.utils import Result

def get_client(login: str, password: str) -> Client:
    client = Client('en-US')
    client.login(auth_info_1=login, password=password)
    client.save_cookies('cookies.json')
    client.load_cookies('cookies.json')
    return client

def load_client() -> Client:
    client = Client('en-US')
    client.load_cookies(path='cookies.json')
    return client

def search_by_user_name(client: Client, user_name: str, num_tweets: int) -> Result[Tweet]:
    user = client.get_user_by_screen_name(user_name)
    tweets = user.get_tweets('Tweets', count=num_tweets)
    return tweets


def search_by_query(client: Client, search: str, product: Literal['Top', 'Latest', 'Media'], num_tweets: int) -> Result[Tweet]:
    if product not in ['Top', 'Latest', 'Media']:
        raise ValueError('Invalid product type. Must be one of: Top, Latest, Media')
    tweets = client.search_tweet(query=search,product=product, count=num_tweets)
    return tweets
