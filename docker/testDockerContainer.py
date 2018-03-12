import requests , json
import config

# 以catalina作为守护进程
# id = '0fecc90b0dbd093de9a0e165b107d97c6336bf989ff35703c9156098b006a52e'
#
# id = '1f3bba183c28016b5496780fe983bd68d74b21fb5396452e9c9228a97ca3dd4f'
# id = '7fe4020c7dc2742dd0f7060dd4e3820940d08d458d800535abc8ac03521f166b'
id = 'ee69f286c63e9f43687c204cb308a70f6c4410c890f53d50146c454f276fd271'
# id = "1f56725dd2dbe5125f36933b286f431e16437521f8e779174ebab4d9d71e016d"
def delete():
    r = requests.delete(config.dockerServer + '/containers/' + id + '')
    print (r.status_code)
    print (r.content)

def start():

    r = requests.post(config.dockerServer + '/containers/' + id + '/start')
    print (r.status_code)
    print (r.content)
def state():
    r = requests.get(config.dockerServer + '/v1.18/containers/' + id + '/json')
    print(r.content)
    print(json.loads(r.content)['State']['Status'])
def create():
    payload = {"Name":"testC",\
               "Cmd": ["/bin/bash", "catalina.sh", "run"], \
               "Image": "tomcat:8.0.47", \
               "ExposedPorts": {"8080/tcp": {}}, \
               "Try": True,"OpenStdin": True, "StdinOnce": False,\
               "HostConfig": {\
                    "Binds": ["/home/fjq/webapps:/usr/local/tomcat/webapps"],\

                    "PortBindings" :\
                        {"8080/tcp" : [{"HostIP" : "0.0.0.0" ,"HostPort" : "11007"}]},\

                } \
            }

    # payload = { {"Binds": ["/usr/jdy/other/:/mnt/software/"], "PortBindings": {"22/tcp": [{"HostPort": "22334"}]}}, "privileged"}
    headers = {'content-type': 'application/json'}
    url = config.dockerServer + '/v1.18/containers/create'
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print('---------------- create content start --------------------')
    print(r.content)

    id = json.loads(r.content)['Id']

    print("id : " + id)
    print('---------------- create content end --------------------')

    print(r.status_code)
def stop():
    r = requests.post(config.dockerServer + '/containers/' + id + '/stop')
    print(r.status_code)
    print(r.content)
# create()

start()
# state()
#
# stop()
# delete()