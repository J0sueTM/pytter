import load_credentials
import client
import user
import query_parser

credLoader = load_credentials
queryParser = query_parser
mainClient = client
mainUser = user

def main():
    # load credentials
    credLoader.writeCredentials()

    # change search query
    queryParser.changeQuery(mainUser.getUserQuery())

    # get search
    mainClient.searchByQuery(queryParser._query)
    
if __name__ == "__main__":
    main()