import requests
import json
x = requests.get("https://poetrydb.org/author").json()
print(x)