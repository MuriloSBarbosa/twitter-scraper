from flask import Flask, request, jsonify
from flask_cors import CORS
from twitter_scraper import get_client, load_client, search_by_query, search_by_user_name
from utils import format_tweets
from exception_handler import handle_exceptions


app = Flask(__name__)
CORS(app)
handle_exceptions(app)

@app.route('/login', methods=['POST'])
def req_login():
    login = request.json['login']
    password = request.json['password']

    get_client(login, password)

    return jsonify({'message': 'Login successful'}), 200

@app.route('/', methods=['GET'])
def req_search_by_query():
    search_input = request.args.get('search')
    product = request.args.get('product')
    num_tweets = request.args.get('numTweets')

    client = load_client()

    tweets = search_by_query(client, search_input, product, num_tweets)

    return jsonify(format_tweets(tweets)), 200

@app.route('/users/<userName>', methods=['GET'])
def req_search_by_user_name(userName):
    num_tweets = request.args.get('numTweets')

    client = load_client()

    tweets = search_by_user_name(client, userName, num_tweets)

    return jsonify(format_tweets(tweets)), 200


if __name__ == '__main__':
    app.run(debug=True)