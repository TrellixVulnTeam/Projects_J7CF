# We need requests module to send HTTP request to API url.
import requests

# API URL
CRYPTO_API_URL = 'https://api.coinmarketcap.com/v1/ticker/'
# IFTTT URL
IFTTT_WEBHOOK_URL = 'https://maker.ifttt.com/trigger/{}/with/key/doClSGz7wEYAeUNVmx4akB'


# Function returns most recent crypto price if crypto_name matches the API.
def get_latest_crypto_price(crypto_name):

    crypto_name = str(crypto_name)
    response = requests.get(CRYPTO_API_URL)  # Sends request to API URL
    response_json = response.json() # Converts JSON response to Dictionary.

# Searching for crypto name in JSON response
    for i in range(len(response_json)):

        if response_json[i]['id'] == crypto_name:
            return round(float(response_json[i]['price_usd']),2)

    return 0

# Function 'hooks' to IFTTT URL and sends there data in JSON format
def post_ifttt_webhook(event, value, crypto_name):

    data = {'value1': value, 'value2': crypto_name}
    ifttt_webhook_url = IFTTT_WEBHOOK_URL.format(event)
    requests.post(ifttt_webhook_url, json=data)


def format_bitcoin_history(bitcoin_history):

    rows = []
    for bitcoin_price in bitcoin_history:
        # Formats the date into a string: '24.02.2018 15:09'
        date = bitcoin_price['date'].strftime('%d.%m.%Y %H:%M')
        price = bitcoin_price['price']

        # <b> (bold) tag creates bolded text
        # 24.02.2018 15:09: $<b>10123.4</b>

        row = '{}: $<b>{}</b>'.format(date, price)
        rows.append(row)

    # Use a <br> (break) tag to create a new line
    # Join the rows delimited by <br> tag: row1<br>row2<br>row3
    return '<br>'.join(rows)





