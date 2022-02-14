import websocket
import json
from datetime import datetime
import sqlite3
import logging

# The problem here is that i dont understant what and how the order book
# Works and what it represent one of the things that i dont get rigth
# is why the order book dont nofify me the orders that has been executed
# and how the market trades behave.
con = sqlite3.connect("order-book-binance.db")
cur = con.cursor()

logging.basicConfig(filename='program.log', encoding='utf-8',
                    level=logging.DEBUG)

rows_inserted = 0

def on_message(ws, message):
    time = datetime.now()
    time = datetime.timestamp(time)
    cur.execute('INSERT INTO order_book VALUES (time, "{message}")')
    con.commit()
    if rows_inserted % 100 == 0:
        logging.info('{rows_inserted} has been inserted on db')

def on_error(ws, error):
    con.close()
    logging.info('and error has occurred : {error}')
    print(error)

def on_close(ws, close_status_code, colos_msg):
    con.close()
    logging.info('the websocket was closed')
    print('the web socket has been closed')

def on_open(ws):
    pass


if __name__ == "__main__":
    logging.info('Start Order Book Logger')
    websocket.enableTrace(True)
    uri = "wss://stream.binance.com/stream?streams=btcusdt@depth"
    ws = websocket.WebSocketApp(uri,
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.run_forever()
