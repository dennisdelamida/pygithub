import requests
from requests.auth import HTTPBasicAuth
login_url = 'https://api2.watttime.org/v2/login'
rsp = requests.get(login_url, auth=HTTPBasicAuth('dence', 'dence@27'))
print(rsp.json())