import requests
import json
from config import db
from model import people

#Data Wrangling

#person = {
#         "name": resp['name']['first'] + ' ' + resp['name']['last'],
#        "email": resp['email'],
#        "username" : resp['login']['username'],
#        "password" : resp['login']['password'],
#        "gender" : resp['gender'],
#        "photo" : resp['picture']['large']
#        }
#adress = {
#    "street": resp['location']['street']['name'],
#    "number": resp['location']['street']['number'],
#    "city": resp['location']['city'],
#    "state": resp['location']['state']}

def update_api():
    #Requesting API and extract dict to report
    resp = requests.get('https://randomuser.me/api/').json()['results'][0]
    create_people(name= resp['name']['first'] + ' ' + resp['name']['last'],
                email= resp['email'],
                username= resp['login']['username'],
                password= resp['login']['password'],
                gender= resp['gender'],
                photo= resp['picture']['large'])
    return resp

def create_people(name,email,username,password,gender,photo):
    #Add a user
    jwk_user = People(name= name,
            email= email,
            username= username,
            password= password,
            gender= gender,
            photo= photo)
    session=db.create_connection()
    session.add(jwk_user)
    session.commit()

def find_people():
    pass

#Query the user
#our_user = session.query(Person).all()

#for person in our_user:
#    print(person.name)
