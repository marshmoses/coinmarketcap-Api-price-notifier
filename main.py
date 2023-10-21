import requests
# a lib.to make https requests to api.sends requests, handles responses, and works with json data.
import json
#(JavaScript Object Notation) data assist decode JSON data into Python 
from requests import Session
#allows to create a session to store headers,parameters for HTTP requests

from pprint import pprint
#pretty-print
class CMC:#trieve data
    def __init__(self, api_key):#initializes and begins a class
        self.apiurl = "https://pro-api.coinmarketcap.com" #gonna be the base URL for all my requests to the cmc api.
        self.headers = {#provide information about the request
            'accept': 'application/json',#Specifies the desired media types json
            'X-CMC_PRO_API_KEY': api_key,#Contains credentials keys for authentication.
        }
        self.session = Session()
        self.session.headers.update(self.headers)#they persist parameters across multiple HTTP requests are consistent even after changing the symbol

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

if __name__ == "__main__":#ensures you run as main sccript
    api_key = '7b968005-a633-41fc-8072-9faff05a06db'  # API key variable=placeholder
    cmc = CMC(api_key) #instance of cmc running apikey as an argument
    
    symbol = input("Enter the cryptocurrency symbol: ").strip().upper()# promps in the terminal and waits for the user to input a value.
    # The user's input = string..strip=removes unnecessary spaces..upper=case-insensitivity.()takes input from terminal to in be used in script
    #checks the value of the symbol
    if symbol == 'ALL':
        data = cmc.getAllcoins()#fetch information about all cryptocurrencie .data stored in data
        pprint(data) #readable format
    else:
        price = cmc.getPrices(symbol)#passes symbl as an arg
        if price is not None:
            print(f"Price of {symbol}: {price}")
        else:
            print(f"Error: Unable to retrieve data for {symbol}.")



