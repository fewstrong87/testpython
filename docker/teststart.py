import requests , json

id = '69129195c748a8469a70ffdd40493d0bde5a5c66b4c8491def00730a26626441'

def start():

    r = requests.post("http://47.92.103.97:2375/containers/" + id + '/start')
    print (r.status_code)
    print (r.content)
def state():
    r = requests.get("http://47.92.103.97:2375/v1.18/containers/" + id + '/json')
    print(r.content)
    print(json.loads(r.content)['State']['Status'])
def create():
    payload = {"Cmd": "/bin/bash", "Image": "nginx.io", "HostConfig": {"Binds": ["/usr/jdy/other/:/mnt/software/"], "PortBindings": {"22/tcp": [{"HostPort": "22334"}]}}}
    headers = {'content-type': 'application/json'}
    url = "http://47.92.103.97:2375/v1.18/containers/create"
    docreate, dostart, dostop, domonitor, dodelete = True, False, False, False, False
    if docreate:
        r = requests.post(url, data=json.dumps(payload), headers=headers)
        print('---------------- create content start --------------------')
        print(r.content)

        id = json.loads(r.content)['Id']

        print("id : " + id)
        print('---------------- create content end --------------------')

        print(r.status_code)

# start()
state()
# create()