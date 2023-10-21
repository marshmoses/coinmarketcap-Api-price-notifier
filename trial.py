from decouple import Config, Csv
import requests
from requests import Session
import json
from pprint import pprint

# Load environment variables from .env
config = Config()
config.read('.env')

class CMC:
    def __init__(self, api_key):
        self.apiurl = "https://pro-api.coinmarketcap.com"
        self.headers = {
            'accept': 'application/json',
            'X-CMC_PRO_API_KEY': api_key,
        }
        self.session = Session()
        self.session.headers.update(self.headers)

    def getAllcoins(self):
        url = self.apiurl + '/v1/cryptocurrency/map'#endpoint used to retrieve info
        r = self.session.get(url)#requests infor on Cmc.
        #holds the response from the API,
        data = r.json()['data']
        return data# returns the extracted data dict

    def getPrices(self, symbol):# fetch the latest price 
        url = self.apiurl + '/v1/cryptocurrency/quotes/latest'#endpoint
        parameters = {'symbol': symbol, 'convert': 'KES' }
        response = self.session.get(url, params=parameters)  # Use 'self.session' here
        if response.status_code == 200:
            data = json.loads(response.text)['data'][symbol]['quote']['KES']['price']#symbol=arg
            return data
        else:
            return None  # Return None if there was an error
# ... (rest of your CMC class remains the same)

if __name__ == "__main__":
    api_key = config('X-CMC_PRO_API_KEY')
    cmc = CMC(api_key)
    
    symbol = input("Enter the cryptocurrency symbol: ").strip().upper()
    
    if symbol == 'ALL':
        data = cmc.getAllcoins()
        pprint(data)
    else:
        price = cmc.getPrices(symbol)
        if price is not None:
            print(f"Price of {symbol}: {price}")
        else:
            print(f"Error: Unable to retrieve data for {symbol}.")









       
