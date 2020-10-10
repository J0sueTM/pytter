import json

global _query
_query = {
    "q": "learn python",
    "result_type": "popular",
    "count": 5,
    "lang": "en"
}

def changeQuery(_new_query):
    try:
        _query = _new_query
    except:
        print("Coudn't change the query")

def writeQuery():
    try:
        # serialize
        with open('./data/twitter_query.json', 'w') as _file:
            json.dump(_query, _file)
            _file.close()

        # deserialize
        with open('./data/twitter_query.json', 'r') as _file:
            return json.load(_file)
    except:
        print("error: Coudn't load query, using memory cache")