import json
import requests
import os 
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get('MY_API_KEY')
print(API_KEY)

request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AMZN&apikey="+ API_KEY

print(request_url)

response = requests.get(request_url)

print("Status:" +  str(response.status_code)) #from class
print("Response Text: " + response.text) #from class

parsed_response = json.loads(response.text)

breakpoint() #from class

print("The Latest Closing Pirce IS: $XYZ.00")

parsed_response["Time Series (Daily)"]["2019-02-19"]["4. close"]

symbol = "NFLX" # TODO: capture user input, like... input("Please specify a stock symbol: ")


# TODO: further revise the example outputs below to reflect real information
print("-----------------")
print(f"STOCK SYMBOL: {symbol}")
print("RUN AT: 11:52pm on June 5th, 2018")
print("-----------------")
print("LATEST DAY OF AVAILABLE DATA: June 4th, 2018")
print(f"LATEST DAILY CLOSING PRICE: {latest_price_usd}")
print("RECENT HIGH: $101,000.00")
print("RECENT LOW: $99,000.00")
print("-----------------")
print("RECOMMENDATION: Buy!")
print("RECOMMENDATION REASON: Because the latest closing price is within threshold XYZ etc., etc. and this fits within your risk tolerance etc., etc.")
print("-----------------")


#need to install pip install python-dotenv

# see: https://www.alphavantage.co/documentation/#daily (or a different endpoint, as desired)
# TODO: assemble the request url to get daily data for the given stock symbol...

# TODO: use the "requests" package to issue a "GET" request to the specified url, and store the JSON response in a variable...

# TODO: traverse the nested response data structure to find the latest closing price and other values of interest...
latest_price_usd = "$100,000.00"

#
# INFO OUTPUTS
#

# TODO: write response data to a CSV file
