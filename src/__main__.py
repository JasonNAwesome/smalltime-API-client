#!/usr/bin/env python3
import sys, time, string
import urllib.request

print('--- Welcome to the CLI bitcoincharts Price-Checker ---')

# Receives Bitcoin Market & Currency
def _user_input():

    market_names = ("bitfinex","bitstamp","btce","itbit")

    for i in range(0,len(market_names)):
        print("-----", market_names[i])
    user_input_market = input('Please choose a Bitcoin market from one above: ')

    # API doesn't seem to support currency anymore
    user_input_currency = "USD"

    input_data = (user_input_market, user_input_currency)
    return input_data

def _get_request(user_tuple, site_url):

    market_name = user_tuple[0]
    currency_name = user_tuple[1]
    site_url += market_name + currency_name

    # Now the long csv file is loaded
    # 41 is the magic number for one line
    bitcoin_string = urllib.request.urlopen(site_url).read(41)

    categories = ("Time : ", "Price: ", "Trade: ")

    #This is where printing the UNIX epoch time, Price, & Trade amount go
    bitcoin_string = bitcoin_string.decode("utf-8").split(',')
    print(categories[0], 
          time.strftime('%Y-%m-%d %H:%M:%S', 
          time.localtime(int(bitcoin_string[0]))))
    for i in range(1,len(categories)):
        # str then float to rid myself of the scourge that is trailing zeroes
        print(categories[i], str(float(bitcoin_string[i])))

def _main():

    site_url = 'http://api.bitcoincharts.com/v1/trades.csv?symbol='

    # Get user input and pass to GET request
    data_tuple = _user_input()

    # GET request
    _get_request(data_tuple, site_url)

if __name__ == '__main__':
    _main()
