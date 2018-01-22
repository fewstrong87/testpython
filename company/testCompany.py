import requests
import json
import config

url = config.platfromApi + '/company/add'
company = {"companyName":"thot","companyNumber" : "321", "serverIp" : "localhost:", "serverPort" : "3304", "remark" : "12345"}
headers={'content-type': 'application/json'}

r = requests.post(url, data=json.dumps(company), headers=headers)
print (r.status_code)
print('---------------- content start --------------------')

print(r.content)

print('---------------- content end --------------------')

if r.status_code == 200:
    print('created success')
else :
    print('created failed')

company ['id'] = json.loads(r.content)['data']['id']

print ("created id is " + company['id'])


url = config.platfromApi + '/platform/company/update'
r = requests.post(url, data=json.dumps(company), headers=headers)


print (r.status_code)
print('---------------- content start --------------------')

print(r.content)

print('---------------- content end --------------------')

if r.status_code == 200:
    print('update success')
else :
    print('update failed')

url = config.platfromApi + '/company/' + company['id'] + '/delete'
r = requests.post(url)

print (r.status_code)
print('---------------- content start --------------------')

print(r.content)

print('---------------- content end --------------------')

if r.status_code == 200:
    print('delete success')
else :
    print('delete failed')