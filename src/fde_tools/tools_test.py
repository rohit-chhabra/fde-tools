import os
import json
from dotenv import load_dotenv
from openai import OpenAI
import sqlite3

load_dotenv(override=True)

openai_api_key = os.getenv('OPENAI_API_KEY')

# Initialization
if(openai_api_key):
    print(f'OpenAI key exists and beings with {openai_api_key[:8]}')
else:
    print('OpenAI key not found')

MODEL = 'gpt-4.1-mini'

openai = OpenAI()

DB = 'prices.db'

with sqlite3.connect(DB) as conn:
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS prices (city TEXT PRIMARY KEY, price REAL)')
    conn.commit

def set_ticket_price(city, price):
    with sqlite3.connect(DB) as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO prices VALUES(?, ?) ON CONFLICT(city) DO UPDATE SET price = ?', (city.lower(), price, price))
        conn.commit()

ticket_prices = [{"city": "london", "price": 400},
{"city": "paris", "price": 500},
{"city": "mumbai", "price": 700},
{"city": "tokyo", "price": 800}]

for item in ticket_prices:
    set_ticket_price(item.city, item.price)

system_message = """
You are a helpful assistant for an Airline called FlightAI.
Give short, courteous answers, no more than 1 sentence.
Always be accurate. If you don't know the answer, say so.
"""
