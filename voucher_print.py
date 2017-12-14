import json
import requests
import time
import datetime

#Parametros de la API de SOCIFI
headers = {'Authorization' : 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXUyJ9.eyJleHAiOjE0OTUzMTcxMjksInVzZXJuYW1lIjoianVhbi5jYXN0aWxsZWphQGdtYWlsLmNvbSIsImlkIjo3NjYzLCJpYXQiOiIxNDk1MjMwNzI5In0.AsHUlALklaUW3QC96U2PbmW8x9UUTlRzeUyj51z5gQHGm3BQElnktrDWZxQe6I59QOvf2xQ8AV4riQQJ1AtrolIZCZq7l3DCCX-ioqiRa9xh-8fBm1hL8SxfWNUPMbHoTRi4rLJ_q2Rqs9lIXChW5oIeSgEtC4MkVuN8l1ysKjJjKtd0EeGOQ9-KUMGILwyOlYvdVDvwgYavoVoiFmH6L3Wkm3oyPNqpsAtL8pvLhF3o553un6N6gwK6lK3FKXLU3LnY1sXsEmKXeU_il1QSwTHKp_CZxJS_FrQ78ndQ4pNoYi_3hdG73ncwKjCE8qyfKz7Q5dIxHNK5qLU1mUy_VSUWQE38rVW1YRAooJK_3QJCDxspI0qKSO6IxeoHV2S3Mzk20gGyshDcKXeulBsmgF44kR1SOmH0s046usuziEZOw7nYVXknAU9EMRT7HSRWfUrv1h3RJfHorcbeGmYBZiLkYvfkWHtu-zBs4s-Y65klkIM3daGuQW_alkVGqe1U3IilIJCzcan_U4QF-jiFglTbnV4MR_05q9UDbkfgUVoq__VsFDaP0KuoHjkAdDMkZIq0dJXOwQZc_a3UHgyDsaN1MxMPJiT0Y6wIsTSK9BfuUDn11F2VlsGf1iRbht6JtDFFQpD_aQ_JnjCZaylS2uHSGWMTREC2PWwQH-5R_Q8'}
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