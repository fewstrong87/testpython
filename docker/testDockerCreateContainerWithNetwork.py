import requests , json
import config

# id = "20eb16aa66339b0fbe2983e5f2f83260643b11ea9f504a477b8379ca9bbc3a62"
id = "0e06f1cbde00bd0c5777f440aa058a1c14bd73b11425525f65a94adac6eccb32"
def create():
    payload = {
               # "Name":"testC",\
               # "Cmd": ["/bin/bash",], \
               "Cmd": ["/bin/bash", "catalina.sh", "run"], \
               # "Cmd": [ "/usr/local/tomcat/bin/catalina.sh",], \
               # "Cmd": ["/usr/local/tomcat/bin/startup.sh", ], \
               "Image": "d2e5f74b7c0e", \
               "ExposedPorts": {"8080/tcp": {}}, \
               "Try": True,"OpenStdin": True, "StdinOnce": False,\
               "HostConfig": {\
                    # "Binds": ["/home/fjq/webapps:/usr/local/tomcat/webapps"], \
                   "Binds": ["/home/fjq/webapps:/z/java/apache-tomcat-8/webapps"], \
                   "PortBindings" :\
                        {"8080/tcp" : [{"HostIP" : "0.0.0.0","HostPort" : "7020"}]},\

                },\
               "NetworkingConfig" : {
                   "EndpointsConfig" : {
                       "zy_nw" : {
                           "IPAMConfig" : {
                               "IPv4Address" : "192.168.20.20",
                               # "LinkLocalIPs" : ["192.168.1.11"]
                           },
                           # "IPAddress" : "192.168.1.20"
                       }
                   }
               }
            }
    # print(json.dumps(payload))
    headers = {'content-type': 'application/json'}
    url = config.dockerServer + '/v1.26/containers/create'
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
    r = requests.get(config.dockerServer + '/v1.26/containers/' + id + '/json')
    print(r.content)
    print(json.loads(r.content)['State']['Status'])
# start()
create()
# info()