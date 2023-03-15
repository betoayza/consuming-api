import requests

url = 'https://dog.ceo/api/breeds/list/all'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(type(data), data)
    f = open("breeds.txt", "wt")
    f.write(str(data))
    f.close()
    
else:
    print('Some error has ocurred')