import base64
import requests
import requests.auth
import json

# get bearer token for application only requests
def get_auth_token():
	consumer_key = "hpeapj"
	#consumer_secret = "yuTIeAPUsAGB"
	consumer_secret = "kfkYCdqrewsj"
	bearer_token_credentials = base64.urlsafe_b64encode(
    	'{}:{}'.format(consumer_key, consumer_secret).encode('ascii')).decode('ascii')
	url = 'https://gmi-apac.iwsinc.com/usermanager/oauth/token?'
	headers = {
    	'Authorization': 'Basic {}'.format(bearer_token_credentials),
    	'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
	}
	data = 'scope=SCOPE_TENANT_ADMIN&grant_type=client_credentials'
	response = requests.post(url, headers=headers, data=data)
	response_data = response.json()
	
	if response_data['token_type'] == 'bearer':
    		bearer_token = response_data['access_token']
    		return bearer_token
	else:
    		raise RuntimeError('unexpected token type: {}'.format(response_data['token_type']))



url = 'https://gmi-apac.iwsinc.com/gmiserver/tenant/hpeapj/app/GoVerifyID/template/'
#payload = {'store_id':'fbc2081d-90aa-41f2-8d23-8b348c10c09b'}
auth_token = get_auth_token()
header = {'Authorization' : 'Bearer {}'.format(auth_token), 'content-type' : 'application/json'}
resp = requests.get(url, headers=header)
if resp.status_code != 200:
	print('Status:', resp.status_code, 'Problem with the request. Exiting.')
#	exit()
# resp ==> <class 'requests.models.Response'>
obj = resp.json() # convert class attribute to obj list
#print (type(obj))

for item in obj:
	print item

print auth_token