import requests
import urllib
import json

header = {'Authorization' : 'Bearer 015d39085399c043958d475b10b1052c7e03a6a0'}
resp = requests.get('https://dclearpass/api/local-user', verify=False, headers=header)
if resp.status_code != 200:
	print('Status:', resp.status_code, 'Problem with the request. Exiting.')
	exit()

print resp.text

print len(resp.text)
print resp.status_code
print resp.headers['content-type']
print resp.headers['Date']
#	raise ApiError('GET /read/ {}'.format(resp.status_code))
