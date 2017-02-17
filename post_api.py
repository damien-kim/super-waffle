import requests
import urllib
import json

payload = {'store_id':'fbc2081d-90aa-41f2-8d23-8b348c10c09b'}
header = {'Authorization' : 'Bearer 015d39085399c043958d475b10b1052c7e03a6a0', 'content-type' : 'application/json'}
resp = requests.post('https://dclearpass/api/extension/instance', verify=False, headers=header, data=json.dumps(payload))
if resp.status_code != 200:
	print('Status:', resp.status_code, 'Problem with the request. Exiting.')
#	exit()

print(resp.text)

print(len(resp.text))
print(resp.status_code)
print(resp.headers['content-type'])
print(resp.headers['Date'])
