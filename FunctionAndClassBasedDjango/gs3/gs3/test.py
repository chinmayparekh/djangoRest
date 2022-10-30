import requests
import json

URL = "http://127.0.0.1:8000/studentapiClass/"


# data = {
#     'id':2,
#     'name': 'Sonam',
#     'roll': 101,
#     'city': 'Ranchi'
# }
#
# json_data = json.dumps(data)
# r = requests.post(url=URL, data=json_data)
#
# data = r.json()
# print(data)
def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    r = requests.get(url=URL, data=json_data)
    data = r.json()
    print(data)


def post_data():
    data = {
        'id': 685,
        'name': 'axel',
        'roll': 55,
        'city': 'delhi'
    }

    json_data = json.dumps(data)
    r = requests.post(url=URL, data=json_data)

    data = r.json()
    print(data)


def update_data():
    data = {
        'id': 1,
        'name': 'Chin',
    }

    json_data = json.dumps(data)
    r = requests.put(url=URL, data=json_data)

    data = r.json()
    print(data)


def delete_data():
    data = {
        'id': 1}

    json_data = json.dumps(data)
    r = requests.delete(url=URL, data=json_data)

    data = r.json()
    print(data)


# update_data()
# get_data()
# delete_data()
post_data()
# get_data()
