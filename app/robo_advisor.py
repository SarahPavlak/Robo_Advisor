import json
import requests
import os 
from dotenv import load_dotenv

load_dotenv()

def to_usd(my_price):
        return "${0:,.2f}".format(my_price) #taken from screencast

API_KEY = os.environ.get('MY_API_KEY')

request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AMZN&apikey="+ API_KEY

print(request_url)

response = requests.get(request_url)

#print("Status:" +  str(response.status_code)) #from class
#print("Response Text: " + response.text) #from class
parsed_response = json.loads(response.text) #from class
tsd = parsed_response["Time Series (Daily)"] #from screencast
dates = list(tsd.keys())
latest_day = dates[0]
last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"] 
latest_close_usd = tsd[latest_day]["4. close"] #from screencast


high_prices = [] 
for date in dates:
    high_price = tsd[date]["2. high"]
    high_prices.append (float(high_price))

recent_high = max(high_prices)

low_prices = [] 
for date in dates:
    low_price = tsd[date]["3. low"]
    low_prices.append (float(low_price))

recent_low = min(low_prices)


parsed_response["Time Series (Daily)"]["2019-02-19"]["4. close"] #type it in the terminal to see it

symbol = "NFLX" # TODO: capture user input, like... input("Please specify a stock symbol: ")

print("-----------------")
print(f"STOCK SYMBOL: {symbol}")
print("RUN AT: 11:52pm on June 5th, 2018") #use date time module
print("-----------------")
print(f"LATEST DAY OF AVAILABLE DATA: {last_refreshed}")
print(f"LATEST DAILY CLOSING PRICE: {to_usd(float(latest_close_usd))}")
print(f"RECENT HIGH: {to_usd(float(recent_high))}") 
print(f"RECENT LOW: {to_usd(float(recent_low))}") 
print("-----------------")
print("RECOMMENDATION: Buy!")
print("RECOMMENDATION REASON: Because the latest closing price is within threshold XYZ etc., etc. and this fits within your risk tolerance etc., etc.")
print("-----------------")

parsed_response["Meta Data"].keys()

#need to install pip install python-dotenv

# TODO: write response data to a CSV file
