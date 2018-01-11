#This Scripts are created in a sequential mode, without functions or def,  for easy lecture and code following
#First obtain the Orgs that the user had access and print in the screen asking the user to select the Org with which to work
#Once the Org is selected, print three options: Get the Clients of the devices in the Org, or Traffic or Link Status
#Depends of the selection, proceed to a second API Call to obtain the Clients, Traffic or Status
#Shows how to handled the API Calls, and how to play with the JSON data
#Created by Juan Castilleja - castille@cisco.com

import json
import requests

#Change to your Meraki API Key
APIKey = "b338813f9218b05ea269e7ed556cc7229a7a0f77"

#HTTPS Header Params
headers = {'X-Cisco-Meraki-API-Key' : APIKey , 'Content-Type' : 'application/json'}


#GET Orgs
url = 'https://dashboard.meraki.com/api/v0/organizations/'
# GET a Meraki
r = requests.get(url, headers=headers)
#Validate if the http request return an 200 means OK, in other case, print the error code
if r.status_code == 200:
    r.json()
    MerakiOrgs = json.loads(r.text)
    len_MerakiOrgs = len(MerakiOrgs)
    ##FIN de creacion array Meraki Inventory
    print ("\n Hola! Estas son las Organizaciones a las cuales tienes acceso:")
    for x in range(0, len_MerakiOrgs):
        print "[" + str(x) + "] \t Org ID: " + str(MerakiOrgs[x]['id']) + "\t Nombre de la Org: " + MerakiOrgs[x]['name']

    while True:
        #Allow the user input and validate that is a number and is in the range
        try:
            acepta = int(raw_input('\nCon que Organizacion quiere continuar? Ingrese numero entre []'))
        except ValueError:
            print "Por favor ingresa un numero"
            continue
        else:
            if acepta >= 0 and acepta <len_MerakiOrgs:
                ID = acepta
                OrgID = MerakiOrgs[ID]['id']
                break
            else:
                continue
else:
    print "Error: " + str(r.status_code)
    print "No se pudo obtener Organizacion de la API Key proporcionada"
    quit()

#GET the Inventory of the Org
url = 'https://dashboard.meraki.com/api/v0/organizations/' + str(OrgID) + '/inventory/'
# GET a Meraki
r = requests.get(url, headers=headers)
if r.status_code == 200:
    r.json()
    Inventory = json.loads(r.text)
    len_Inventory = len(Inventory)
else:
    print "Error: " + str(r.status_code)
    print "No se pudo obtener el inventario de la Organizacion"
    quit()

#Truco para borrar pantalla sin depender de OS
print "\n" * 100
print "Que desea obtener de la Organizacion:"
print "\n1.- Clientes"
print "\n2.- Trafico"
print "\n3.- Disponibilidad"
while True:
    #Allow user input and continue with the selected option
    acepta = raw_input('\nIngrese el numero de la seleccion deseada (1,2,3): ')
    if acepta == "1":
        #Create a second GET to obtain CLIENTS of each device in the inventory
        for x in range(0, len_Inventory):
            url = 'https://dashboard.meraki.com/api/v0/devices/' + Inventory[x]['serial'] + '/clients?timespan=86400'
            # GET a Meraki
            r = requests.get(url, headers=headers)
            if r.status_code == 200:
                r.json()
                Clients = json.loads(r.text)
                len_Clients = len(Clients)
                print "Clientes de Equipo: " + Inventory[x]['serial']
                for y in range(0, len_Clients):
                    print "Description: " + Clients[y]['description']
                    print "mdnsName: " + str(Clients[y]['mdnsName'])
                    print "dhcpHostname: " + Clients[y]['dhcpHostname']
                    print "Usage Sent: " + str(Clients[y]['usage']['sent'])
                    print "Usage Received: " + str(Clients[y]['usage']['recv'])
                    print "MAC: " + Clients[y]['mac']
                    print "IP: " + Clients[y]['ip']
                    print "Switch Port: " + str(Clients[y]['switchport'])
                    print "\n"
            else:
                print "Codigo de Error: " + str(r.status_code)
                print "Mensaje: "
                print Clients
        break
    elif acepta == "2":
        # Create a second GET to obtain TRAFFIC of each device in the inventory
        for x in range(0, len_Inventory):
            if Inventory[x]['networkId'] == None:
                break
            else:
                url = 'https://dashboard.meraki.com/api/v0/networks/' + Inventory[x]['networkId'] + '/traffic?timespan=86400'
                # GET a Meraki
                r = requests.get(url, headers=headers)
                if r.status_code == 200:
                    r.json()
                    Traffic = json.loads(r.text)
                    len_Traffic = len(Traffic)
                    print "Trafico de  Equipo: " + Inventory[x]['serial']
                    for y in range(0, len_Traffic):
                        print "Application: " + Traffic[y]['application']
                        print "Destination: " + str(Traffic[y]['destination'])
                        print "Protocol: " + Traffic[y]['protocol']
                        print "Port: " + str(Traffic[y]['port'])
                        print "Sent: " + str(Traffic[y]['sent'])
                        print "Received: " + str(Traffic[y]['recv'])
                        print "Num Clients: " + str(Traffic[y]['numClients'])
                        print "Active Time: " + str(Traffic[y]['activeTime'])
                        print "Flows: " + str(Traffic[y]['flows'])
                        print "\n"
                else:
                    print "Codigo de Error: " + str(r.status_code)
                    print "Mensaje: "
                    print Traffic
                print "\n"
        break
    elif acepta == "3":
        # Create a second GET to obtain Uplink Status of each device in the inventory
        for x in range(0, len_Inventory):
            if Inventory[x]['networkId'] == None:
                break
            else:
                url = 'https://dashboard.meraki.com/api/v0/networks/' + Inventory[x]['networkId'] + '/devices/' + Inventory[x]['serial'] + '/uplink'
                # GET a Meraki
                r = requests.get(url, headers=headers)
                if r.status_code == 200:
                    r.json()
                    Uplink = json.loads(r.text)
                    len_Uplink = len(Uplink)
                    print "Status para Equipo: " + Inventory[x]['serial']
                    for y in range(0, len_Uplink):
                        print "Interface: " + Uplink[y]['interface']
                        if Uplink[y]['status'] == "Active":
                            print "Status: " + Uplink[y]['status']
                            print "IP: " + Uplink[y]['ip']
                            print "Gateway: " + Uplink[y]['gateway']
                            print "Public IP: " + Uplink[y]['publicIp']
                            print "DNS: " + Uplink[y]['dns']
                            print "Using Static IP: " + str(Uplink[y]['usingStaticIp'])
                        else:
                            print "Status: " + Uplink[y]['status']
                        print "\n"
                else:
                    print "Codigo de Error: " + str(r.status_code)
                    print "Mensaje: "
                    print Uplink
                print "\n"
        break
    else:
        print ("\nIngrese el numero de la seleccion deseada (1,2,3): ")
print "\n \n Gracias por utilizar este Script"
