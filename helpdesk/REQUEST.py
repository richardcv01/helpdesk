import json
from helpdesk.settings import *
import requests
from django.core.exceptions import ObjectDoesNotExist

from tikets.models import Tikets
ip = IP_config

def GET_tikets(number):
    request_type = "GET"
    data = {"email": "email", "name": "name"}
    api_url = "http://" + ip + ":80/tikets/"+number
    response = requests.get(api_url)
    print(response.text)

def get_id_user(name_user):
    request_type = "GET"
    api_url = "http://" + ip + ":80/users/" + name_user
    response = requests.get(api_url)
    res = json.loads(response.text)
    return res["user_"]["id"]

def get_stan_tiket(number):
    request_type = "GET"
    api_url = api_url = "http://" + ip + ":80/tikets/" + number + "/"
    response = requests.get(api_url)
    res = json.loads(response.text)
    return res['tikets']["tikets_implementation"]['implementation_text']

def UPDATE_tikets(number, status, id_user):
    #{"pk": id, "tikets_implementation": {"id": tikets_implementation_id, "implementation_text": "1"}, "tikets_Owner": 2}
    headers = {'Content-Type': "application/json; charset=UTF-8", 'Accept': "application/json"}
    data = '{"pk": '+ number + ', "tikets_implementation": {"id": '+ status +', "implementation_text": "1"}, "tikets_Owner": {"id":"'+ str(id_user) +'", "username": "ALL"}}'
    api_url = "http://" + ip + ":80/tikets/" + number + "/"
    print(type(data), number)
    tiket = Tikets.objects.filter(pk=number)
    print('tiket', tiket)
    if not tiket.exists():
        return None
    else:
        try:
            requests.put(api_url, data=data, headers=headers)
            return 1
        except ObjectDoesNotExist as E:
            print(E)
            #return None
        print('update', data)
    #return
