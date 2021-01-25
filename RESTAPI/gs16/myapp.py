import requests
import json

url = "http://127.0.0.1:8000/api/"


def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    headers = {'content-Type': 'application/json'}
    json_data = json.dumps(data)
    r = requests.get(url=url, headers=headers, data=json_data)
    data = r.json()
    print(data)


# get_data()


def post_data():
    data = {
        'name': "test user 6",
        'roll': 106,
        'city': "Aleska",
    }
    headers = {'content-Type': 'application/json'}
    json_data = json.dumps(data)
    r = requests.post(url=url, headers=headers, data=json_data)
    data = r.json()
    print(data)


post_data()


def update_data():
    data = {
        "id": 1,
        'name': "test user 1",
        'city': "Dhaka",
    }
    headers = {'content-Type': 'application/json'}
    json_data = json.dumps(data)
    r = requests.put(url=url, headers=headers, data=json_data)
    data = r.json()
    print(data)

# print("Before: ")
# get_data()
# update_data()
# print("After: ")
# get_data()


def delete_data():
    data = {'id':6}
    headers = {'content-Type': 'application/json'}
    json_data = json.dumps(data)
    r = requests.delete(url=url, headers=headers, data=json_data)
    data = r.json()
    print(data)


# print("Before: ")
# get_data()
# delete_data()
# print("After: ")
# get_data()
