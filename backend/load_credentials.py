import json
import os.path

# macros
api_credentials = {} 
api_credentials["CONSUMER_KEY"] = ""
api_credentials["CONSUMER_SECRET"] = ""
api_credentials["ACCESS_TOKEN"] = ""
api_credentials["ACCESS_SECRET"] = ""
api_credentials["BEARER_TOKEN"] = ""

def writeCredentials():
    if not os.path.exists('./credentials/twitter_credentials.json'):
        try:
            with open('./credentials/twitter_credentials.json', 'w') as _file:
                json.dump(api_credentials, _file)
        except:
            print("Error: Couldn't write credentials on file")

            exit()
