import functions
import time
# Time module is needed to set notifications delay
from datetime import datetime

def main():

    crypto_name = input('What crypto price would you like to follow?: ')
    price = functions.get_latest_crypto_price(crypto_name)

    if price == 0:
        print ('Could not find currency.')
        return 0

    delay = float(input('How often would you like to receive notifications?(min): '))
    print ('Check your telegram!')

    bitcoin_history = []

    while True:

        date = datetime.now()
        # Adds elements to bitcoin_history dictionary
        bitcoin_history.append({'date': date, 'price': price})

        if len(bitcoin_history) == 1:

            # Calls IFTTT function
            functions.post_ifttt_webhook('Crypto_price', functions.format_bitcoin_history(bitcoin_history), crypto_name)

            bitcoin_history = []

        time.sleep(delay*60) # Makes a delay

if __name__ == '__main__':
   main()
