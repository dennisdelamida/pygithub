import requests
from requests.auth import HTTPBasicAuth

login_url = 'https://api2.watttime.org/v2/login'
token = requests.get(login_url, auth=HTTPBasicAuth('dence', 'dence@27')).json()['token']

data_url = 'https://api2.watttime.org/v2/data'
headers = {'Authorization': 'Bearer {}'.format(token)}
params = {'ba': 'CAISO_NORTH', 
          'starttime': '2021-02-20T16:00:00-0800', 
          'endtime': '2021-02-20T16:15:00-0800'}
rsp = requests.get(data_url, headers=headers, params=params)
print(rsp.text)
