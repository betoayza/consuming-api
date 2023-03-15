import requests

url = 'https://dog.ceo/api/breeds/list/all'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(type(data), data)
else:
    print('Some error has ocurred')