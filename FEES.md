# Calculating Total Venmo Fees

Venmo let's you lookup your transaction history [here](https://venmo.com/account/settings/balance) but they don't provide a convenient format from exporting your entire Venmo history as a CSV file.

First you need to clone this repository. Then go [here](https://venmo.com/account/settings/balance) in Google Chrome. Open the Developer Tools (cmd + option + i) and go to the network tab. Click the "View" button and you should see a fetch request to `api.venmo.com`. Right click on that row, Copy > Copy as cURL. Create a file in this repo called `secret.txt` and paste that string into that file. Save.

Then run `python scrape.py` and it will print out a list of all transactions, any associated fees, and give you the sum total.
