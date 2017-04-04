import requests
import random

# # GET REQUEST
# payload = {'designee':'ALL'} # URL QUERY PARAM TEST
# r = requests.get('https://fourthdimensiontestapi.herokuapp.com/tasks/', params=payload)
# print(r.url)
# print(r.json())

# # POST REQUEST
# payload = {'completed':'false', 'label':'Test', 'description': 'testing script post', 'designee':'david','types': 'OTHERS' }
# r = requests.post('https://fourthdimensiontestapi.herokuapp.com/tasks/', data=payload)
# print(r.url)
# print(r.json())

# # PUT REQUEST
# complete = {'completed':'true', }
# r = requests.put('https://fourthdimensiontestapi.herokuapp.com/tasks/11/', data=complete)
# print(r.url)
# print(r.json())


# # POST REQUEST
# for x in range(15):
#     label = 'dummy'
#     rand_person = random.choice(['david','mofi','jun','jabir'])
#     rand_types = random.choice(['OTHERS','CLEANING','COMPUTER','DELIVERY','TRAVEL'])
#     # print(rand_person,rand_types)
#     payload = {'completed':'false', 'label':label, 'description':'dummy post', 'designee': rand_person, 'types': rand_types }
#     r = requests.post('https://fourthdimensiontestapi.herokuapp.com/tasks/', data=payload)
#     # print(r)
#     # print(r.url)
#     # print(r.json())

for task_id in range(14, 29):
    complete = random.choice([True,False])
    if complete:
        complete = {'completed':'true', }
        r = requests.put('http://localhost:8000/tasks/{0}/'.format(task_id), data=complete)
        print(r.url)
        print(r.json())