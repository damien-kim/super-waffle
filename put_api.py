import requests
import urllib
import json

url = 'https://dclearpass/api/extension/instance/c847e00f-f861-4248-bd78-b42c8cd631ea/config'
payload = {'kasada':'https:\\portal.kasada.io','alias':'eGhaHTIs-0dEg-gnCi-PoLs-DaJycbUCb44V','apiKey':'6PJR3ZpiEt88AoBDrEUjF8Qds',"factorsNormal":"[\u0027fingerprint\u0027]","factorsMedium":"[\u0027fingerprint\u0027,\u0027photoLock\u0027]","factorsHigh":"[\u0027fingerprint\u0027,\u0027photoLock\u0027,\u0027gridLock\u0027]","eventProxy":"ep:10010",'debug':'true'}

#payload = {'alias':'eGhaHTIs-0dEg-gnCi-PoLs-DaJycbUCb44V','apiKey':'6PJR3ZpiEt88AoBDrEUjF8Qds'}
header = {'Authorization' : 'Bearer 015d39085399c043958d475b10b1052c7e03a6a0', 'content-type' : 'application/json'}
resp = requests.put(url, verify=False, headers=header, data=json.dumps(payload))
if resp.status_code != 200:
	print('Status:', resp.status_code, 'Problem with the request. Exiting.')
#	exit()

print(resp.text)

print(len(resp.text))
print(resp.status_code)
print(resp.headers['content-type'])
print(resp.headers['Date'])
