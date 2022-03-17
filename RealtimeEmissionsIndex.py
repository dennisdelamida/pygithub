import requests
from requests.auth import HTTPBasicAuth

login_url = 'https://api2.watttime.org/v2/login'
token = requests.get(login_url, auth=HTTPBasicAuth('dence', 'dence@27')).json()['token']

index_url = 'https://api2.watttime.org/index'
headers = {'Authorization': 'Bearer {}'.format(token)}
params = {'ba': 'CAISO_NORTH'}
rsp=requests.get(index_url, headers=headers, params=params)
print(rsp.text)
