import requests
import json
url = 'http://127.0.0.1:8000/stucreate/'
data = {
    'name': 'Mohinee',
    'roll': 101,
    'city': 'Rajshahi',
}
json_data=json.dumps(data)
r=requests.post(url=url,data=json_data)
data=r.json()
print(data)