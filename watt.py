import requests
register_url = 'https://api2.watttime.org/v2/register'
params = {'username': 'dence',
         'password': 'dence@27',
         'email': 'dadelamida@gmail.com',
         'org': 'freds world'}
rsp = requests.post(register_url, json=params)
print(rsp.text)