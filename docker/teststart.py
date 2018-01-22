import requests , json
import config
id = 'e583234b021d581beff11362d4b99a218e3a9d86d0356f2d7fe62568bc46260a'


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
    payload = {"Cmd": "/bin/bash", "Image": "nginx.io", "Try": True,"OpenStdin": True, "StdinOnce": False,\
               "HostConfig": {"Binds": ["/usr/jdy/other/:/mnt/software/"]}}
    # payload = { {"Binds": ["/usr/jdy/other/:/mnt/software/"], "PortBindings": {"22/tcp": [{"HostPort": "22334"}]}}, "privileged"}
    headers = {'content-type': 'application/json'}
    url = config.dockerServer + '/v1.18/containers/create'
    docreate, dostart, dostop, domonitor, dodelete = True, False, False, False, False
    if docreate:
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
# start()
# stop()
# state()
# create()
delete()