import requests

""" r=requests.get('https://randomuser.me/api/')
data=r.json()
result=data['results'][0]
gender=result['gender'] """
male=[]
fmale=[]
s=''
i=0
while i<2:
    r=requests.get('https://randomuser.me/api/')
    data=r.json()
    result=data['results'][0]
    gender=result['gender']
    if gender=='male':
        name=result['name']
        age=result['dob']
        fullname=name['first']+" "+name['last']+" "+str(age['age'])
        male.append(fullname)
        i+=1

print(male)