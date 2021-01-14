import requests
import json

url = "http://127.0.0.1:8000/api/"


def get_data(id=None):
    data = {}
    if id is not None:
        data = {"id": id}
    json_data = json.dumps(data)
    r = requests.get(url=url, data=json_data)
    data = r.json()
    return data


# print(get_data())




def post_data():
    data = {
        'name': "Alvee",
        'roll': 151,
        'city': "Dhaka",
    }
    json_data = json.dumps(data)
    r = requests.post(url=url, data=json_data)
    data = r.json()
    print(data)


# post_data()


def update_data():
    data = {
        'id': 11,
        'name':'Al Minhaz Alzee',
        'roll':130,
        'city': "Savar",
    }
    json_data = json.dumps(data)
    r = requests.put(url=url, data=json_data)
    data = r.json()
    return data


# print(update_data())

def delete_data():
    data = {'id': 10}
    json_data = json.dumps(data)
    r = requests.delete(url=url, data=json_data)
    data = r.json()
    print(data)


delete_data()
