import csv
import requests

with open('import_csv_template.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    url = "https://example.okta.com/api/v1/users?activate=false"
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'SSWS XXX'
    }

    for row in reader:

        payload = {
            'profile': {
                'login': row['login'],
                'firstName': row['firstName'],
                'lastName': row['lastName'],
                'email': row['email'],
                'title': row['title'],
                'displayName': row['displayName'],
                'primaryPhone': row['primaryPhone'],
                'streetAddress': row['streetAddress'],
                'city': row['city'],
                'state': row['state'],
                'zipCode': row['zipCode'],
                'countryCode': row['countryCode'],
                'organization': row['organization'],
                'department': row['department'],
                'shortName': row['shortName']
            },
            'credentials': {
                "password": {
                    "value": "Apple123!"
                }
            }
        }

        response = requests.request("POST", url, headers=headers, json = payload)

print(response.text.encode('utf8'))