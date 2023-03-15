import requests

url = 'https://dog.ceo/api/breeds/list/all'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()['message'] # parse JSON to Python Map
    
    print(type(data), data)

    data2 = []

    for x in data.items():
        print(x[0])        
        print(x[1])
        data2.append(f"{x[0]} : {x[1]}")
      
    f = open("breeds.txt", "wt")
    f.write(str(data2))
    f.close()
    
else:
    print('Some error has ocurred')