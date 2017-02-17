import requests, json
import urllib


url = 'https://dclearpass/api/extension/instance/c847e00f-f861-4248-bd78-b42c8cd631ea/config'
#payload = {'store_id':'fbc2081d-90aa-41f2-8d23-8b348c10c09b'}
header = {'Authorization' : 'Bearer 015d39085399c043958d475b10b1052c7e03a6a0', 'content-type' : 'application/json'}
resp = requests.get(url, verify=False, headers=header)
if resp.status_code != 200:
	print('Status:', resp.status_code, 'Problem with the request. Exiting.')
#	exit()

#print(resp.text, resp.headers)
print(resp.text.encode('utf-8', 'ignore'))

print(len(resp.text))
print(resp.status_code)
print(resp.headers['content-type'])
print(resp.headers['Date'])
