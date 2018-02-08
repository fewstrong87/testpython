import requests , json
import config

# id = "20eb16aa66339b0fbe2983e5f2f83260643b11ea9f504a477b8379ca9bbc3a62"
id = "8e41705a95c0323c994d7e6fb1d45a4d8fe319183f6bb9196158b76a507a990c"
def create():
    payload = {"StdinOnce":False,"Try":True,"Image":"a92c139758db","ExposedPorts":{"8080/tcp":{}},"Cmd":["/bin/bash","catalina.sh","run"],"HostConfig":{"Binds":["/home/fjq/webapps:d:/weappsP/11da29e9db574977b9527d31016a79b0"]},"OpenStdin":True}

    # payload = { {"Binds": ["/usr/jdy/other/:/mnt/software/"], "PortBindings": {"22/tcp": [{"HostPort": "22334"}]}}, "privileged"}
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

def json1(): #e57a762d2f27
    r = requests.get(config.dockerServer + '/containers/json')
    print(r.status_code)
    print(r.content)

start()
# create()
# json1()