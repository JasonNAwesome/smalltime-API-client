#!/usr/bin/python
import sys, time, string
import urllib.request

print('Welcome to the simple CLI Bitcoin API.')

def _main():

    site_url = 'http://api.bitcoincharts.com/v1/trades.csv?symbol='

    # Get user input and pass to GET request
    data_tuple = _user_input()

    # GET request
    _get_request(data_tuple, site_url)


# Receives Bitcoin Market & Currency
def _user_input():

    currency_names = ("KRW","NMC","IDR","RON","ARS","AUD",
                    "BGN","BRL","BTC","CAD","CHF","CLP",
                    "CNY","CZK","DKK","EUR","GAU","GBP",
                    "HKD","HUF","ILS","INR","JPY","LTC",
                    "MXN","NOK","NZD","PEN","PLN","RUB",
                    "SAR","SEK","SGD","SLL","THB","UAH",
                    "USD","XRP","ZAR")

    market_names = ("bitfinex","bitstamp","btce","itbit","anxhk",
                    "hitbtc","kraken","bitkonan","bitbay","rock",
                    "cbx","cotr","vcx")

    print(market_names)
    user_input_market = input('Please choose a Bitcoin market from one above: ')
    print(currency_names)
    user_input_currency = input('Please choose a currency from one above: ')

    input_data = (user_input_market, user_input_currency)
    return input_data

def _get_request(user_tuple, site_url):

    market_name = user_tuple[0]
    currency_name = user_tuple[1]
    site_url += market_name + currency_name

    # Now the long csv file is loaded
    # 41 is the magic number for one line
    bitcoin_price = urllib.request.urlopen(site_url).read(41)

    categories = ("Time |", "Price|", "Trade Amount|")

    #This is where printing the UNIX epoch time, Price, & Trade amount go
    bitcoin_price = bitcoin_price.decode("utf-8").split(',')
    print(categories[0], time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(bitcoin_price[0]))))
    for i in range(1,len(categories)):
        print(categories[i], bitcoin_price[i])

if __name__ == '__main__':
    _main()
