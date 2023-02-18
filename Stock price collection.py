import yfinance as yf
import pandas as pd
import time
import csv

# Define the ticker symbol
tickerSymbol = '^DJI'

# Define the filename to save the data
filename = 'dji_prices.csv'

# Define the time interval for updates (in seconds)
update_interval = 60

# Get the last timestamp in the CSV file
try:
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        last_row = list(csv_reader)[-1]
        last_timestamp = pd.to_datetime(last_row[0])
except (FileNotFoundError, IndexError):
    last_timestamp = None
    
# Download historical data for the past 7 days with a 1-minute interval
historicalData = yf.download(tickerSymbol, period='7d', interval='1m')

# Append historical data to the file if it's not already in there
if last_timestamp is None or last_timestamp < historicalData.index[0]:
    with open(filename, 'a', newline='') as file:
        csv_writer = csv.writer(file)
        for index, row in historicalData.iterrows():
            if last_timestamp is None or index > last_timestamp:
                csv_writer.writerow([index.strftime('%Y-%m-%d %H:%M:%S'), row['Close']])
    last_timestamp = historicalData.index[-1]

while True:
    # Get the data for the past 1 minute
    tickerData = yf.download(tickerSymbol, period='1d', interval='1m').tail(1)

    # Append new data to the file
    with open(filename, 'a', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow([tickerData.index[0].strftime('%Y-%m-%d %H:%M:%S'), tickerData['Close'][0]])
    last_timestamp = tickerData.index[0]

    # Wait for the specified interval before updating the file again
    time.sleep(update_interval)
