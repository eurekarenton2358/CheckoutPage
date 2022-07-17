

import requests
import json
import webbrowser
import ast
api_url = "https://api.sandbox.checkout.com/payments"
todo = {
    "source": {
        "type": "sofort"
    },
    "amount": 44600,
    "currency": "EUR",
    "reference": "request-05"
         }
headers = {"Content-Type":"application/json",
            "Authorization":"sk_test_0b9b5db6-f223-49d0-b68f-f6643dd4f808"}
response = requests.post(api_url, data=json.dumps(todo), headers=headers)
content=response.json()
print(content)

link=json.dumps(content)
json=json.loads(link)
website=json['_links']['redirect']['href']

webbrowser.open(website)











