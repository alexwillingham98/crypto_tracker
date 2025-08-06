from dotenv import load_dotenv
import os
import requests

load_dotenv()
token = os.getenv("COINGECKO_TOKEN")


def get_price(id):

    

    url = "https://api.coingecko.com/api/v3/simple/price"

    headers = {
        "accept": "application/json",
        "token": token
    }

    data = {
        "vs_currencies" : "usd",
        "ids": id
    }

    response = requests.get(url, headers=headers, params=data)
    print(response.text)

def get_top_100_coins():

    url = "https://api.coingecko.com/api/v3/coins/markets"

    headers = {
    "accept": "application/json",
    "token": token
    }

    data = {
        "vs_currency" : "usd"
    }

    response = requests.get(url, headers=headers, params=data)
    return response.json()


