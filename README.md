# carnitickets

## Quickstart
To run the `ticketConter.py` script, first install the necessary Google API dependencies using `pip`. Directions for doing so can be found [here](https://developers.google.com/sheets/api/quickstart/python#step_1_install_the_google_client_library).

Next, ensure that in the same directory as the `ticketCounter.py` script there are three files:

1. `Orders.csv` -- This is the csv file downloaded from Wix whose format can be found on the [OrderFileFormat](https://github.com/jrosner1/carnitickets/wiki/OrderFileFormat) wiki page.
2. `token.json` -- Use the [Oath client ID credentials guide](https://developers.google.com/workspace/guides/create-credentials#oauth-client-id) to obtain access credentials.

Now, populate the `sheet_list` list in the `ticketCounter.py` file with valid [Teamname, google_url] pairs. The list is populated as an example. See the format for the google sheets on the [SheetFormat](https://github.com/jrosner1/carnitickets/wiki/SheetFormat) wiki.

Now you are ready to run the script!

## Algorithm
![image](https://user-images.githubusercontent.com/38009477/188511130-7bbbbb07-36e6-48a1-a1e6-a254e6116f09.png)

## Troubleshooting
See the Google [python quickstart](https://developers.google.com/sheets/api/quickstart/python) for more in-depth tips and setup.
