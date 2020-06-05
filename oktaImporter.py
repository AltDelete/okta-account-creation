import csv
import requests

with open('example.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    url = "https://demokit.okta.com/api/v1/users?activate=false"
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'SSWS 00d5uThYKGfoQ6boWyqMZIH4TxSAGvbyMemazNA9tf'
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

        # payloadString = str(payload)
        # payload = "{\n  \"profile\": {\n    \"firstName\": " + row[firsName] + ",\n    \"lastName\": \"Brock\",\n    \"email\": \"isaac@pretendco.com\",\n    \"login\": \"isaac@pretendco.com\",\n    \"shortName\": \"isaac\"\n  },\n  \"credentials\": {\n    \"password\" : { \"value\": \"{{Apple123!}}\" }\n  }\n}"

        # # print(row['primaryPhone'], row['department'])
        # # print(payloadString)
        response = requests.request("POST", url, headers=headers, json = payload)




# response = requests.request("POST", url, headers=headers, data = payload)

print(response.text.encode('utf8'))