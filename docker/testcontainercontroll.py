import requests
import json
import config

url = config.dockerApi + '/containers/create'
# payload = {"Cmd" : "/bin/bash" , "Image" : "docker.io/alpine:latest", "HostConfig": { "Binds": ["/tmp:/tmp"]}, "PortBindings": { "22/tcp": [{ "HostPort": "11022" }] },"Binds": ["/tmp:/tmp"]}
headers={'content-type': 'application/json'}



docreate, dostart, dostop, domonitor, dodelete = True, True, False, True, False
if docreate:
    cc = {"image":"nginx.io","companyId":"10"}

    r = requests.post(url, data=json.dumps(cc), headers=headers)
    print('---------------- create content start --------------------')
    print(r.content)

    id = json.loads(r.content) ['data']['id']

    print ("id" + id)
    print('---------------- create content end --------------------')

    if(r.status_code == 200):
        print ( "create success")
    else:
        print ( "create failed")
else :
    id = '09b1dbc08a9e4c9bb6a8a58351013132'
if domonitor:
    r = requests.get(config.dockerApi + '/containers/monitor/' + id)
    print('---------------- monitor content start --------------------')
    print(r.content)
    # cc = {"id":"7bcb6fc643634a5ab85023e7c04e691a","containerId":"82ece58d42f9af5d628165d013117c4eea46387e81b99624ed968ff21125334e","companyId":"32"}

    print('---------------- monitor content end --------------------')

    if(r.status_code == 200):
        print ( "monitor success")
    else:
        print ( "monitor failed")


if dostart:
    r = requests.post(config.dockerApi + '/containers/' + id + '/start')
    print('---------------- start content start --------------------')
    print(r.content)
    # cc = {"id":"7bcb6fc643634a5ab85023e7c04e691a","containerId":"82ece58d42f9af5d628165d013117c4eea46387e81b99624ed968ff21125334e","companyId":"32"}

    print('---------------- start content end --------------------')

    if(r.status_code == 200):
        print ( "start success")
    else:
        print ( "start failed")

if dostart:
    r = requests.get(config.dockerApi + '/containers/monitor/' + id)
    print('---------------- start end status start --------------------')
    print(r.content)
    # cc = {"id":"7bcb6fc643634a5ab85023e7c04e691a","containerId":"82ece58d42f9af5d628165d013117c4eea46387e81b99624ed968ff21125334e","companyId":"32"}

    print('---------------- start end status end --------------------')



if dostop:
    r = requests.post(config.dockerApi + '/containers/' + id + '/stop')
    print('---------------- stop content start --------------------')
    print(r.content)
    # cc = {"id":"7bcb6fc643634a5ab85023e7c04e691a","containerId":"82ece58d42f9af5d628165d013117c4eea46387e81b99624ed968ff21125334e","companyId":"32"}

    print('---------------- stop content end --------------------')

    if(r.status_code == 200):
        print ( "stop success")
    else:
        print ( "stop failed")

if dostop:
    r = requests.get(config.dockerApi + '/containers/monitor/' + id)
    print('---------------- stop end status start --------------------')
    print(r.content)
    # cc = {"id":"7bcb6fc643634a5ab85023e7c04e691a","containerId":"82ece58d42f9af5d628165d013117c4eea46387e81b99624ed968ff21125334e","companyId":"32"}

    print('---------------- stop end status end --------------------')



if dodelete:

    r = requests.post(config.dockerApi + '/containers/' + id + '/delete')

    data = json.loads(r.content)

    print(data)

    if (r.status_code == 200):
        print("delete success")
    else:
        print("delete failed")

