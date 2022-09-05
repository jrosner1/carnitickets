# carnitickets

## Quickstart
To run the `ticketConter.py` script, first install the necessary Google API dependencies using `pip`. Directions for doing so can be found [here](https://developers.google.com/sheets/api/quickstart/python#step_1_install_the_google_client_library).

Next, ensure that in the same directory as the `ticketCounter.py` script there are three files:

1. `Orders.csv` -- This is the csv file downloaded from Wix whose format can be found on the [OrderFileFormat]() wiki page.
2. `credentials.json` and ``token.json`` -- Use the [Oath client ID credentials guide](https://developers.google.com/workspace/guides/create-credentials#oauth-client-id) to obtain access credentials.

## Algorithm

```mermaid
flowchart TD
  Start --> Stop
  Stop --> Next
```
