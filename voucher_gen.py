import json
import requests
import time
import datetime

#Parametros de la API de SOCIFI
headers = {'Authorization' : 'Bearer '}

#Array de planes y PlanID de SOCIFI API
planName = ["Null", "Bronce", "Plata", "Oro"]
planPrice = ["0", "$50", "$100", "$150"]
planID = ["0", "19087", "19088", "19089"]

#Seleccionar codigo a generar
print ("Bienvenido al sistema de asignacion de codigos de Ruralnet \n") + ("Seleccione el tipo de codigo de acceso a generar: \n")
print ("1.- Plan Bronce: $50 pesos \t Un dia de navegacion. 1 Mbps ")
print ("2.- Plan Plata: $100 pesos \t Catorce dias de navegacion. 3 Mbps")
print ("3.- Plan Oro: $150 pesos \t Treinta dias de navegacion. 10 Mbps \n")
print ("Seleccione el tipo de Plan (introduciendo el numero del plan, ejemplo '2', genera codigo para Plan Plata \n")

plan_input = input('Plan Seleccionado [1,2,3]: ')

print ("\n Usted ha seleccionado el tipo de plan " + planName[plan_input] + " y se generara un cargo de " + planPrice[plan_input])
acepta = raw_input('Esta Usted de acuerdo? (S/N): ')
if acepta=="S":
     #print planID[plan_input]
    print ("Generando el codigo, por favor espere... \n")
    url = 'https://admin-api.socifi.com/users/7663/pay-thru/vouchers'
    data = {'payThruPlanId' : planID[plan_input], 'multiDevice' : 1 , 'prefix' : 'Ruralnet', 'discount' : 100, 'count' : 1, 'length' : 10, 'type' : 'alpha', 'expiresAt' : '2017-12-31T23:59:59+00:00'}
    r = requests.post(url, headers=headers,data=data)
    r.json()
    json_data = json.loads(r.text)
    #Se obtiene el SetId del Voucher
    voucherSetId = json_data['voucherSetId']
    voucherSetId = str(voucherSetId)
    #Se genera GET para traer el Voucher
    url = 'https://admin-api.socifi.com/users/7663/pay-thru/vouchers/' + voucherSetId
    r = requests.get(url, headers=headers)
    r.json()
    json_data = json.loads(r.text)
    metadata = json_data['metadata']
    vouchers = metadata['vouchers']
    code = vouchers[0]
    print ("\n El codigo para el plan " + planName[plan_input] + " es: " + code['code'])
    print ("\n \n Gracias por preferir Ruralnet =)")
    print ("\n Adios \n Script by castille@cisco.com ")
elif acepta=="N":
     print ("\n Adios \n Script by castille@cisco.com")
else:
     print ("Introduzca S/N:")



