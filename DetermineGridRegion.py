import requests
from requests.auth import HTTPBasicAuth

login_url = 'https://api2.watttime.org/v2/login'
token = requests.get(login_url, auth=HTTPBasicAuth('dence', 'dence@27')).json()['token']

region_url = 'https://api2.watttime.org/v2/ba-from-loc'
headers = {'Authorization': 'Bearer {}'.format(token)}
params = {'latitude': '42.372', 'longitude': '-72.519'}
rsp=requests.get(region_url, headers=headers, params=params)
print(rsp.text)