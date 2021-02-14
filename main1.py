import requests

r=requests.get('https://randomuser.me/api/?results=5')
r_gen=requests.get('https://randomuser.me/api/?gender=2')
date=r_gen.json()['results']
for i in date:
    print(i)