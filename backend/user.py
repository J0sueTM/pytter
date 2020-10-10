import query_parser

user_query = query_parser._query

def getUserQuery():
    _open = True

    while _open:
        try:
            for qr in user_query:
                print(f"insert {qr}:", end = " ")

                user_query[qr] = input()

                _open = False
        except:
            print("error: Coudn't address the query, would you like to try again? [y][n]")

            if str(input()) != 's':
                _open = False

    return user_query