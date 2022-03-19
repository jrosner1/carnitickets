from __future__ import print_function
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import csv

SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

sheet_list = [
    ['FINDING_DORY', '12tJdPMmUPscgNfBjhW4r1muTH2MRn8JbC5E1IH4oLUo'],
    ['BOOTY_FEAST', '1vRBpDEYK7PTwWG8OLfnzR1axkd2zuB5FtnvrKgq0TIY'],
    ['INSTANT_RAW', '1AvORD2SSjgnOjnp6Je9gKb-NlYdb_uF1M4Iz1h4hVRw'],
    ['MILWAUKEE', '1pjj3wuRV48VdP8jAOubnUFcR3_4z4hKrC0pxlEzQsdw'],
    ['GLUCK', '1GPxcNhnofyQLY4kRbJi4-aSF3kXLgK9_iZm5eCtjEX0'],
    ['SPIDERMAN', '16O-_ivG4O9aXTl_WLYi3wUE_flx8okJ6jlCCyXURuZE'],
    ['JIZZ', '1YZFIXLdc8Bmj_S52Yp60Dvv_fTVCnFawxeG9HWcW3rw'],
    ['RIM', '1IzqDvQd_HC9VrYfGevkpn9avjxoZtbF7IbUwTq0aUuo'],
    ['PINK_SPANKS', '1PHAW6R_BlZ5ugxNBv1bYaU0pVkJK0JLICjACxaRwI9A'],
    ['DICKEY','1yYlnLF5cyi7gQR3mEWkkwAEog4LNvVipX7P9lQbaA9Y']
]

def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    #Get a list of all order names
    num_orders = -1
    order_name_list = []
    count = 0
    just_name_list = []
    with open('orders.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if not count == 0:
                order_name_list.append([first_initial_last_name(row[1].upper()), int(row[0]), False])
                num_orders += int(row[0])
            count += 1

    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    try:
        with open('unmatched.txt', 'w') as f:
            #f.write('readme')
            service = build('sheets', 'v4', credentials=creds)
            # Call the Sheets API
            num_matched = 0
            for i in sheet_list:
                sheet = service.spreadsheets()
                result = sheet.values().get(spreadsheetId=i[1],
                                            range='Team Roster!B:B').execute()
                values = result.get('values', [])

                if not values:
                    print('No data found.')
                    return
                team_members = 0
                for row in values[2:]:
                    for name in order_name_list:
                        if len(row) > 0 and first_initial_last_name(row[0].upper()) == name[0]:
                            name[2] = True
                            team_members += name[1]
                            num_matched += name[1]
                print("Team " + i[0] + " has " + str(team_members) + " tickets ordered.")
            for i in order_name_list:
                if i[2] == False:
                    f.write(i[0] + '\n')
            print("There are " + str(num_orders - num_matched) + " tickets that the program could not match with someone on a team")
        

    except HttpError as err:
        print(err)


def first_initial_last_name(name):
    name = name.split()
    return name[0][0] + name[-1]


if __name__ == '__main__':
    main()

