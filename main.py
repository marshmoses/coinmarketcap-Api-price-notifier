import requests
import api
from pprint import pprint as pp

class CMC:
    def __init__(self, api_key):
        self.apiurl = "https://pro-api.coinmarketcap.com"
        self.headers = {
            'accept': 'application/json',
            'X-CMC_PRO_API_KEY': api_key,
        }
        self.session = requests.Session()
        self.session.headers.update(self.headers)

    def getAllcoins(self):
        url = self.apiurl + '/v1/cryptocurrency/map'
        r = self.session.get(url)
        data = r.json()['data']
        return data
    

    def getPrices(self,symbol):
        url=self.apiurl + '/v2/cryptocurrency/quotes/latest'
        parameters={'symbol' :symbol}
        r = self.session.get(url,params=parameters)
        data = r.json()['data']
        return data


if __name__ == "__main__":
    cmc = CMC(api.API_KEY)
    #this get all coins listed in cmc
   # pp(cmc.getAllcoins())
   #the below gets (prices,market cap,%,platforms to trade in and pairs to be compared with etc)
    pp(cmc.getPrices('BTC'))
#the above code getsall coins with(name,slug,symbol and tokken address)




