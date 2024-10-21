import requests

# Función para obtener el precio de Bitcoin
def get_bitcoin_price():
    response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd')
    return response.json().get('bitcoin', {}).get('usd', 0)

# Función para obtener el precio del oro
def get_gold_price():
    response = requests.get('https://metals-api.com/api/latest?access_key=YOUR_API_KEY&base=XAU&symbols=USD')
    return response.json().get('rates', {}).get('USD', 0)

# Función para obtener el precio de la plata
def get_silver_price():
    response = requests.get('https://metals-api.com/api/latest?access_key=YOUR_API_KEY&base=XAG&symbols=USD')
    return response.json().get('rates', {}).get('USD', 0)

# Puedes agregar más funciones para petróleo y trigo
