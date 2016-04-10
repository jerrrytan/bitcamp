#Author: Harrison

import requests
import json
import math

customerId = '5709786a319313dd1b438fd0'
apiKey = 'cf6fe22672e82008e57d304ac6e0d669'

#Get the amount of money in the food bank account
def getFoodAmount():
    r = requests.get('http://api.reimaginebanking.com/accounts/57097f4a319313dd1b43b2bd?key=cf6fe22672e82008e57d304ac6e0d669')
    return json.loads(r.text)['balance']

#clear the food bank account
def clearFood():
    payload = {
        "medium": "balance",
        "payee_id": "570986c4319313dd1b43b2e9",
        "amount": getFoodAmount(),
        "transaction_date": "2016-04-09",
        "status": "completed",
        "description": "string"
    }

    res = requests.post(
        'http://api.reimaginebanking.com/accounts/57097f4a319313dd1b43b2bd/transfers?key=cf6fe22672e82008e57d304ac6e0d669',
        data=json.dumps(payload),
        headers={'content-type':'application/json'},
    )

#Get the amount of money in the person's bank account
def getBankAmount():
    r = requests.get('http://api.reimaginebanking.com/accounts/57097a02319313dd1b43b29d?key=cf6fe22672e82008e57d304ac6e0d669')
    return json.loads(r.text)['balance']

#Transfer x percent of money from bank account to food bank account
def percentFood(percent):
    amount = getBankAmount()

    payload = {
        "medium": "balance",
        "payee_id": "57097f4a319313dd1b43b2bd",
        "amount": math.floor(amount*percent/100),
        "transaction_date": "2016-04-09",
        "status": "completed",
        "description": "string"
    }

    requests.post(
        'http://api.reimaginebanking.com/accounts/57097a02319313dd1b43b29d/transfers?key=cf6fe22672e82008e57d304ac6e0d669',
        data=json.dumps(payload),
        headers={'content-type':'application/json'},
    )

    return math.floor(percent*amount/100)
