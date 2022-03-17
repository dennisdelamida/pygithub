import requests
from requests.auth import HTTPBasicAuth

login_url = 'https://api2.watttime.org/v2/login'
token = requests.get(login_url, auth=HTTPBasicAuth('dence', 'dence@27')).json()['token']

forecast_url = 'https://api2.watttime.org/v2/forecast'
headers = {'Authorization': 'Bearer {}'.format(token)}
params = {'ba': 'NYISO_NYC', 
          'starttime': '2021-08-05T09:00:00-0400', 
          'endtime': '2021-08-05T09:05:00-0400'}
rsp = requests.get(forecast_url, headers=headers, params=params)
print(rsp.text)
