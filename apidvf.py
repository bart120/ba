import requests

code_commune="01450"
size = 100
api_root=" http://api.cquest.org/dvf"
url_api = f"{api_root}?code_commune=" + f"{code_commune}"
print(url_api)
req = requests.get(url_api)
wb = req.json()
print(wb)