import requests , json , config


def all() :
    url = config.eomsDockerServer + '/images/getAllImageWithDocker'
    r = requests.get(url)
    print( ' statuscode ' , r.status_code)
    print( ' content ', r.content)

def create():
    headers = {'content-type': 'application/json'}
    url = config.eomsDockerServer + '/images/create'

    payload = {
        "name" : "tomcat1",
        "type" : "tomcat1",
        "imageId" : "sha256:3fa822599e10c5f2080dcf647068c72022b111d31bbec0c5adb8a96e7eb5379b"
    }

    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(r.status_code)
    print(r.content)

def update():
    headers = {'content-type': 'application/json'}
    url = config.eomsDockerServer + '/images/update'

    payload = {
        "id" : "32edea4ab9e945e1b43c61ea9ff25949",
        "name": "tomcat4",
        "type": "tomcat4",
        "imageId": "sha256:3fa822599e10c5f2080dcf647068c72022b111d31bbec0c5adb8a96e7eb5379b"
    }

    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(r.status_code)
    print(r.content)

# create()
# update()
all()