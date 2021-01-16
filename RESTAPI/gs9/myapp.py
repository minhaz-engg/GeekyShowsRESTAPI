import requests
import json

url = "http://127.0.0.1:8000/api/"


def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    headers = {'content-Type': 'application/json'}
    json_data = json.dumps(data)
    r = requests.get(url=url,headers=headers, data=json_data)
    data = r.json()
    print(data)


get_data()


def post_data():
    data = {
        'name': "Minhaz Chowdhury",
        'roll': 100,
        'city': "Rajshahi",
    }
    headers = {'content-Type': 'application/json'}
    json_data = json.dumps(data)
    r = requests.post(url=url, headers=headers, data=json_data)
    data = r.json()
    print(data)


# post_data()