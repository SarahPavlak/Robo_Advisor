import csv 
import json
import requests
import os 
from dotenv import load_dotenv

load_dotenv()

def to_usd(my_price):
        return "${0:,.2f}".format(my_price) #taken from screencast

API_KEY = os.environ.get('MY_API_KEY')

user_input = "MSFT" #todo: Capture user input
request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=" + user_input + "&apikey=" + API_KEY

print(request_url)

response = requests.get(request_url)

parsed_response = json.loads(response.text) #from class
tsd = parsed_response["Time Series (Daily)"] #from screencast
dates = list(tsd.keys()) #from screencast
latest_day = dates[0] #from screencast
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

symbol = user_input 

#csv_file_path = "data/prices.csv"

csv_file_path = os.path.join (os.path.dirname(__file__), "data", "prices_" + user_input + ".csv")
csv_header = ["timestamp", "open", "low", "high", "close", "volume"]

with open(csv_file_path, "w") as csv_file:
        writer = csv.DictWriter (csv_file, fieldnames = csv_header)

        for date in dates:
            daily_prices = tsd[date]

            writer.writerow({
                "timestamp": date,  
                "open": daily_prices["1. open"],
                "high": daily_prices["2. high"], 
                "low": daily_prices["3. low"],
                "close": daily_prices["4. close"], 
                "volume": daily_prices["5. volume"] 
        })


print("-----------------")
print(f"STOCK SYMBOL: {symbol}")
print("RUN AT: 11:52pm on June 5th, 2018") #use date time module
print("-----------------")
print(f"LATEST DAY OF AVAILABLE DATA: {last_refreshed}")
print(f"LATEST DAILY CLOSING PRICE: {to_usd(float(latest_close_usd))}")
print(f"RECENT HIGH: {to_usd(float(recent_high))}") 
print(f"RECENT LOW: {to_usd(float(recent_low))}") 
print("-----------------")
print("RECOMMENDATION: Buy!") #todo this part
print("RECOMMENDATION REASON: Because the latest closing price is within threshold XYZ etc., etc. and this fits within your risk tolerance etc., etc.") #todo this part
print("-----------------")
print("WRITING DATA TO CSV: {csv_file_path}")
print("-----------------")

parsed_response["Meta Data"].keys()

#need to install pip install python-dotenv
#at 1:04


#todo:
# time stamp 
# data visualizations of closing price over time?
#make readme file
#The system should prompt the user to input one or more stock symbols (e.g. "MSFT", "AAPL", etc.). It may optionally allow the user to specify multiple symbols, either one-by-one or all at the same time (e.g. "MSFT, AAPL, GOOG, AMZN"). It may also optionally prompt the user to specify additional inputs such as risk tolerance and/or other trading preferences, as desired and applicable.
#Before requesting data from the Internet, the system should first perform preliminary validations on user inputs. For example, it should ensure stock symbols are a reasonable amount of characters in length and not numeric in nature.
#If preliminary validations are not satisfied, the system should display a friendly error message like "Oh, expecting a properly-formed stock symbol like 'MSFT'. Please try again." and stop execution.
#When the system makes an HTTP request for that stock symbol's trading data, if the stock symbol is not found or if there is an error message returned by the API server, the system should display a friendly error message like "Sorry, couldn't find any trading data for that stock symbol", and it should stop program execution, optionally prompting the user to try again.
#If the system processes only a single stock symbol at a time, the system may use a single CSV file named "data/prices.csv", or it may use multiple CSV files, each with a name corresponding to the given stock symbol (e.g. "data/prices_msft.csv, "prices_aapl.csv", etc.). If the system processes multiple stock symbols at a time, it should use multiple files, each with a name corresponding to the given stock symbol (e.g. "data/prices_msft.csv", "prices_aapl.csv", etc.). If using more than one CSV file, the program should have a way of cleaning-up to prevent uncontrolled proliferation of new files.








