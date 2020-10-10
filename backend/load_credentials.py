import json
import os.path

# macros
api_credentials = {} 
api_credentials["CONSUMER_KEY"] = "CzKMJIHewYU8brmh0neTflE5i"
api_credentials["CONSUMER_SECRET"] = "10CGMXLfRtUd3Y2yIRlIXwT5Yg84YGod9OdKfJlzdTvKExacYD"
api_credentials["ACCESS_TOKEN"] = "1137817457941516288-eVqNEdLZowVUhN7v0EaTJNDZ8ViYXZ"
api_credentials["ACCESS_SECRET"] = "WgjL7wr1eTlQxwqP566MfWql8cBqHkgQcnF4SbI4fZS8J"
api_credentials["BEARER_TOKEN"] = "AAAAAAAAAAAAAAAAAAAAAHrhIQEAAAAArxQxNOB78ABd0GgAQAo3ywi3vSs%3DmQL8GISP87Sf1FPgASIoMbbaHNKsgJKQmvTJRiroiJ3SPCqVrX"

def writeCredentials():
    if not os.path.exists('./credentials/twitter_credentials.json'):
        try:
            with open('./credentials/twitter_credentials.json', 'w') as _file:
                json.dump(api_credentials, _file)
        except:
            print("Error: Couldn't write credentials on file")

            exit()