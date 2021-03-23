import requests, pprint

host = '10.31.70.210'
login = 'restapi'
password = 'j0sg1280-7@'

url = 'https://' + host + ':55443'

r = requests.post(url + '/api/v1/auth/token-services', auth=(login, password), verify=False)

token = r.json()["token-id"]

header = {"content-type": "application/json", "X-Auth-Token": token}

r = requests.get(url + '/api/v1/interfaces', headers=header, verify=False)

pprint.pprint(r.json())
