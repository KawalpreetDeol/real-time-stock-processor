import yfinance as yf
import time
from kafka import KafkaProducer
import json

STOCK_SYMBOL = 'AAPL'
KAFKA_TOPIC = 'stock_data'
KAFKA_SERVER = 'localhost:9092'

producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER,
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

def fetch_stock_data():
    stock = yf.Ticker(STOCK_SYMBOL)
    data = stock.history(period='1d', interval='1m')
    return data

while True:
    stock_data = fetch_stock_data()
    for timestamp, row in stock_data.iterrows():
        record = {
            'symbol': STOCK_SYMBOL,
            'timestamp': timestamp.strftime('%Y-%m-%d %H:%M:%S'),
            'open': row['Open'],
            'high': row['High'],
            'low': row['Low'],
            'close': row['Close'],
            'volume': row['Volume']
        }
        producer.send(KAFKA_TOPIC, value=record)
    time.sleep(60)  # Fetch data every minute

producer.close()
