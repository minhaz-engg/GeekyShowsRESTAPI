import requests
import json
url = "http://127.0.0.1:8000/api/"
r = requests.get(url=url)
data = r.json()
print(data)
