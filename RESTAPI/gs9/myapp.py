import requests
import json
url = "http://127.0.0.1:8000/api/"


def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    r = requests.get(url=url, data=json_data)
    data = r.json()
    print(data)


def post_data(data):
    headers={'content-Type':'application/json'}
    json_data = json.dumps(data)
    r = requests.post(url=url,headers=headers, data=json_data)
    data = r.json()
    print(data)






post_d = {
        'name': "Mohinee Kisku",
        'roll': 101,
        'city': "Rajshahi",
    }


post_data(post_d)
# get_data()