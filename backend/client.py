import requests
from requests_oauthlib import OAuth1
import json

# TODO add more paths
endpoint_paths = {
    "search": f"search/tweets.json",
    "ver_account": "account/verify_credentials.json"
}
current_endpoint = "search"

protocol = "https://"
domain = "api.twitter.com/"
api_version = "1.1/"
endpoint_path = endpoint_paths[current_endpoint]
endpoint = f"{protocol}{domain}{api_version}{endpoint_path}"


def loadCredentialsAndAuthenticate():
    try:
        with open('./credentials/twitter_credentials.json', 'r') as _file:
            _auth = json.load(_file)

        return OAuth1(
            _auth['CONSUMER_KEY'],
            _auth['CONSUMER_SECRET'],
            _auth['ACCESS_TOKEN'],
            _auth['ACCESS_SECRET']
        )
    except:
        print("Error: Couldn't load credentials")

# search
def searchByQuery(_query):
    current_response = requests.get(
        endpoint,
        {
            "q": _query['q'],
            "result_type": _query['result_type'],
            "count": _query['count'],
            "lang": _query['lang']
        },
        auth = loadCredentialsAndAuthenticate()
)

    try:
        # serialize
        with open('./data/search/current_search.json', 'w') as _file:
            json.dump(current_response.json(), _file)

            _file.close()

        # deserialize
        with open('./data/search/current_search.json', 'r') as _file:
            query_search = json.load(_file)

            _file.close()

        count = 1
        for query_result in query_search['statuses']:
            # TODO output file for frontend client access
            output = """
{}
from: {}

text: {}

likes: {}

retweets: {}
            """.format(
                count,
                query_result['user']['name'],
                query_result['text'],
                query_result['favorite_count'],
                query_result['retweet_count']
            )

            print(output)

            count += 1

        return query_search
    except:
        print("Error: Coudn't write and load query")