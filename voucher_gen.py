import json
import requests
import time
import datetime

#Parametros de la API de SOCIFI
headers = {'Authorization' : 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXUyJ9.eyJleHAiOjE0OTUzMTcxMjksInVzZXJuYW1lIjoianVhbi5jYXN0aWxsZWphQGdtYWlsLmNvbSIsImlkIjo3NjYzLCJpYXQiOiIxNDk1MjMwNzI5In0.AsHUlALklaUW3QC96U2PbmW8x9UUTlRzeUyj51z5gQHGm3BQElnktrDWZxQe6I59QOvf2xQ8AV4riQQJ1AtrolIZCZq7l3DCCX-ioqiRa9xh-8fBm1hL8SxfWNUPMbHoTRi4rLJ_q2Rqs9lIXChW5oIeSgEtC4MkVuN8l1ysKjJjKtd0EeGOQ9-KUMGILwyOlYvdVDvwgYavoVoiFmH6L3Wkm3oyPNqpsAtL8pvLhF3o553un6N6gwK6lK3FKXLU3LnY1sXsEmKXeU_il1QSwTHKp_CZxJS_FrQ78ndQ4pNoYi_3hdG73ncwKjCE8qyfKz7Q5dIxHNK5qLU1mUy_VSUWQE38rVW1YRAooJK_3QJCDxspI0qKSO6IxeoHV2S3Mzk20gGyshDcKXeulBsmgF44kR1SOmH0s046usuziEZOw7nYVXknAU9EMRT7HSRWfUrv1h3RJfHorcbeGmYBZiLkYvfkWHtu-zBs4s-Y65klkIM3daGuQW_alkVGqe1U3IilIJCzcan_U4QF-jiFglTbnV4MR_05q9UDbkfgUVoq__VsFDaP0KuoHjkAdDMkZIq0dJXOwQZc_a3UHgyDsaN1MxMPJiT0Y6wIsTSK9BfuUDn11F2VlsGf1iRbht6JtDFFQpD_aQ_JnjCZaylS2uHSGWMTREC2PWwQH-5R_Q8'}

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


# while True:
#     print ("\n")
#     a = input('Quiere generar otro codigo? (S/N)')
#     if a=="S":
#         # Pedir el SERIAL del Device
#         serial = input('Enter the Network of the Meraki device: ')
#         url = 'https://n164.meraki.com/api/v0/networks/' + network + '/traffic'
#
#         # GET a Meraki
#         r = requests.get(url, headers=headers, params=payload)
#         r.json()
#         json_data = json.loads(r.text)
#         # Validar que Meraki responda OK al GET
#         if r.status_code == 200:
#             pprint.pprint(json_data)
#         else:
#             print("Error al obtener la API")
#
#         continue
#     elif a=="N":
#         print ("\n Script by castille@cisco.com")
#         break
#     else:
#         print("Introduzca S/N")
