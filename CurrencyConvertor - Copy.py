## Imports 
from requests import get
from pprint import PrettyPrinter
from requests.models import Response
######################################

API_KEY = 'ae8797629314e2956861'
BASE_URL = 'https://free.currconv.com/'
printer = PrettyPrinter()

# Get fulll list of currencies
def get_currencies():
    endpoint = f"api/v7/currencies?apiKey={API_KEY}"
    url = BASE_URL+ endpoint
    data = get(url).json()["results"]
    data = list(data.items())
    data.sort()
    return data

#print Currencies
def print_currencies(currencies):
    for name, currency in currencies:
        name = currency["currencyName"]
        _id = currency["id"]
        symbol = currency.get("currencySymbol","")
        print(f"{_id}-{name} - {symbol}")

# Getting Exchange rate
def exchange_rate(currency1, currency2):
    endpoint = f"api/v7/convert?q={currency1}_{currency2}&compact=ultra&apiKey={API_KEY}"
    url = BASE_URL + endpoint
    response = get(url)
    data = response.json()
    if len(data) == 0:
        print("Invalid currencies.")
        return 
    rate = list(data.values())[0]
    print(f"{currency1} --> {currency2} = {rate}")
    return rate

# convert
def convert(currency1, currency2,amount):
    rate = exchange_rate(currency1,currency2)
    if rate is None:
        return
    try:
        amount = float(amount)
    except:
        print("Invalid amount!")
        return
    converted_amount = rate * amount
    print(f"{amount} {currency1} = {converted_amount} {currency2}")
    return converted_amount

def main():
    currencies = get_currencies()
    print("Hello to the Currency converter!")

    while True:
        print("List - lists the diffrenct currencies")
        print("Convert - converts from one currency to another")
        print("Rate- gets the convertion rate of to currencies")
        print("q - to quit the progrem")
        command = input("Enter a command: ").lower()

        if command == 'q':
            break
        elif command == 'list':
            print_currencies(currencies)
        elif command == 'convert':
            currency1 = input("Enter a base currency: ").upper()
            amount = input(f"Enter amount in {currency1} to convert: ")
            currency2 = input("Enter currency to convert to: ").upper()
            convert(currency1=currency1,currency2=currency2,amount=amount)
        elif command == 'rate':
            currency1 = input("Enter a base currency: ").upper()
            currency2 = input("Enter a currency to convert to: ").upper()
            exchange_rate(currency1 = currency1, currency2 = currency2)
        else:
            print("Invalid Command!")

main()
