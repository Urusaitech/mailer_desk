import requests
from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json


def call_kraken_free():
    resp = requests.get('https://api.kraken.com/0/public/Ticker?pair=xbtusd')
    price = resp.json()
    price = price['result']['XXBTZUSD']['a']
    price = int(round(float(price[0]), 1))
    price = str(price)
    return f'{price} USD'


# https://pro.coinmarketcap.com/account/
def call_cmc():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    parameters = {
        'slug': 'bitcoin',
        'convert': 'USD'
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': '888a5eb0-4065-4691-8c43-4bfdd0af3adf',
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)['data']['1']['quote']['USD']['price']
        data = str(int(round(data, 1)))
        return f'{data} USD'
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
        return f'limit'
