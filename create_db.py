import sqlite3

# connect to the sqlite db
connection = sqlite3.connect('app.db')

# make cursor object to execute SQL queries
cursor = connection.cursor()

# create stock table
cursor.execute('''CREATE TABLE stock (
        id INTEGER PRIMARY KEY,
        symbol TEXT NOT NULL UNIQUE,
        company TEXT NOT NULL
        );''')

# create stock price table
cursor.execute('''CREATE TABLE stock_price (
        id INTEGER PRIMARY KEY,
        stock_id INTEGER,
        date NOT NULL,
        open NOT NULL,
        high NOT NULL,
        low NOT NULL,
        close NOT NULL,
        adjusted_close NOT NULL,
        volume NOT NULL,
        FOREIGN KEY (stock_id) REFERENCES stock (id)
        );''')

connection.commit()