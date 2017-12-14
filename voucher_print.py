import json
import requests
import time
import datetime

#Parametros de la API de SOCIFI
headers = {'Authorization' : 'Bearer '}
#payload = {'timespan' : '7200'}

url = 'https://admin-api.socifi.com/users/7663/pay-thru/vouchers/213'
# GET a SOCIFI
#r = requests.get(url, headers=headers, params=payload)
r = requests.get(url, headers=headers)
r.json()
json_data = json.loads(r.text)
metadata = json_data['metadata']
vouchers = metadata['vouchers']
code = vouchers[0]
code = str(code)
# Validar que Meraki responda OK al GET
if r.status_code == 200:
    #print json.dumps(json_data)
    print code['code']
else:
    print ("Error al obtener la API")
