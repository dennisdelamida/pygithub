import requests
from requests.auth import HTTPBasicAuth
from os import path

login_url = 'https://api2.watttime.org/v2/login'
token = requests.get(login_url, auth=HTTPBasicAuth('dence', 'dence@27')).json()['token']

maps_url = 'https://api2.watttime.org/v2/maps'
headers = {'Authorization': 'Bearer {}'.format(token)}
rsp=requests.get(maps_url, headers=headers)

cur_dir = path.dirname(path.realpath('__file__'))
file_path = path.join(cur_dir, 'wt_map.geojson')
with open(file_path, 'wb') as fp:
    fp.write(rsp.content)
