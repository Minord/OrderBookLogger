import websocket
import json
from datetime import datetime
import sqlite3
import logging

con = sqlite3.connect("order-book-binance.db")
cur = con.cursor()

logging.basicConfig(filename='program.log', level=logging.DEBUG)

rows_inserted = 0

def on_message(ws, message):
    global rows_inserted
    time = datetime.now()
    time = datetime.timestamp(time) 
    cur.execute(f'INSERT INTO order_book VALUES ({time}, \'{message}\');')
    con.commit()
    rows_inserted += 1
    if rows_inserted % 100 == 0:
        logging.info(f'{rows_inserted} has been inserted on db')

def on_error(ws, error):
    logging.info(f'an error has occurred : {error}')
    print(error)

def on_close(ws, close_status_code, colos_msg):
    logging.info('the websocket was closed')

def on_open(ws):
    pass


if __name__ == "__main__":
    logging.info('Start Order Book Logger')
    uri = """wss://stream.binance.com/stream?streams=btcusdt@depth"""
    ws = websocket.WebSocketApp(uri,
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.run_forever()
    con.close()
