import requests
import json
import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base

#Create DB conection
engine = db.create_engine('mysql+mysqlconnector://dba:pegasos93@localhost:3306/rbsdb', echo = True)


#Requesting API and extract dict to report
resp = requests.get('https://randomuser.me/api/').json()['results'][0]

#Data Wrangling
person = {
         "name": resp['name']['first'] + ' ' + resp['name']['last'],
        "email": resp['email'],
        "username" : resp['login']['username'],
        "password" : resp['login']['password'],
        "gender" : resp['gender'],
        "photo" : resp['picture']['large']
        }
adress = {
    "street": resp['location']['street']['name'],
    "number": resp['location']['street']['number'],
    "city": resp['location']['city'],
    "state": resp['location']['state']
}
print(person)
print(adress)