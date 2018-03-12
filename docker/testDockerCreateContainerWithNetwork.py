import requests , json
import config

id = "7db32f1c784da659b444afc6742e152c72a509e0558a0b44e96228c0556e1410"
# id = "28d7142ca5fff10f1aa90e46e563726f85d74317a7ac086eb69df238933fdb20"
def create():
    payload = {
               "Cmd": ["/bin/bash"],
               "Image": "sha256:d2e5f74b7c0ec189416d8dd957a660913fe28b45b91b91bda3960b595e721274",
               "ExposedPorts": {"8080/tcp": {}},
               "Try": True,"OpenStdin": True, "StdinOnce": True,
               "HostConfig": {
                   "Binds": ["/usr/hjzy/webapp:/opt/tomcat/apache-tomcat-8.0.24/webapps"],
                   # "PortBindings" :
                        # {"8080/tcp" : [{"HostPort" : "50127"}]},

                },
               "NetworkingConfig" : {
                   "EndpointsConfig" : {
                       "zy_nw" : {
                           "IPAMConfig" : {
                               "IPv4Address" : "192.168.20.102"
                           },
                       }
                   }
               }
            }
    # print(json.dumps(payload))
    headers = {'content-type': 'application/json'}
    url = config.dockerServer + '/v1.24/containers/create'
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print('---------------- create content start --------------------')
    print(r.content)

    id = json.loads(r.content)['Id']

    print("id : " + id)
    print('---------------- create content end --------------------')

    print(r.status_code)
def start():

    r = requests.post(config.dockerServer + '/containers/' + id + '/start')
    print (r.status_code)
    print (r.content)

def delete():
    r = requests.delete(config.dockerServer + '/containers/' + id + '')
    print (r.status_code)
    print (r.content)

def start():

    r = requests.post(config.dockerServer + '/containers/' + id + '/start')
    print (r.status_code)
    print (r.content)
def state():
    r = requests.get(config.dockerServer + '/v1.24/containers/' + id + '/json')
    print(r.content)
    print(json.loads(r.content)['State']['Status'])
start()
# delete()
# create()
# state()