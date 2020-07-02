import os
import json
import requests
from urllib.request import Request, urlopen


def exec_sql(sql_query: str):
    url = f"{os.getenv('HASURA_URL')}/query"
    payload = json.dumps({
        "type": "run_sql",
        "args": {
            "sql": sql_query
        }
    })
    headers = {
        "Content-Type": "application/json",
        "X-Hasura-Admin-Secret": os.getenv('HASURA_SECRET')
    }

    req = requests.post(url, headers=headers, data=payload)
    resp = req.json()
    head = resp["result"][0]
    data = resp["result"][1:]
    for i in range(len(data)):
        data[i] = dict(zip(head, data[i]))
    return data

class Hasura:
    def __init__(self, address, secret):
        self.address = address
        self.secret = secret

    def query(self, string):
        url = self.address
        payload = json.dumps({
            "query": string
        })
        payload = '{"query":"' + string + '"}'
        headers = {
            "content-type": "application/json",
            "x-hasura-admin-secret": self.secret
        }
        req = requests.post(url, headers=headers, data=payload)
        response = req.json()
        return response
