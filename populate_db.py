import sqlite3
import alpaca_trade_api as tradeapi

connection = sqlite3.connect('app.db')
cursor = connection.cursor()

api = tradeapi.REST('PKE7MYUB832V9GO9C7LQ', 'v1YeASYxqMR3oKKnDBJhjfcc1FQtMt3hJrN7kqKV', api_version='v2', base_url='https://paper-api.alpaca.markets')
assests = api.list_assets()

for assest in assests:
    # print(assest)
    try:
        if assest.status == 'active' and assest.tradable == True:
            cursor.execute('INSERT INTO stock (symbol, company) VALUES (?, ?)', (assest.symbol, assest.name))
    except Exception as e:
        print(assest.name)
        print(e)



connection.commit()