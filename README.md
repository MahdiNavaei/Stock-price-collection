# Stock-price-collection

Hello friends

Today I wrote a code that I thought was interesting, and wanted to share with you.

One important thing to me was to get the prices of a stock with the API of a site and save it in a CSV file so that I could use it later to predict its growth or decline in the market, like forex.

One of the challenges I faced was that I wanted these prices to be updated by the minute and saved in the same CSV file at the end of the file.

The following code does the same thing! I am extracting the price growth of DJI stock for the last 7 days with the help of Yahoo Finance's API, and then this program adds a new price to this file every minute.

This helps to calculate the growth trend of this share or any other share whose data has been collected later with this data.

The point was that the APIs were only free for 7 days with a time step of one minute.
