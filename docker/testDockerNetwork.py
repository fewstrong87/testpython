import requests, json
import config

id = '4500adecbab8d91fec263d0672029366a54808e69b8ae91729abff7f886e40a0'


def create():
    networks = {
        "Name": "zy_nw",
        "CheckDuplicate": False,
        "Driver": "bridge",
        "EnableIPv6": False,
        "IPAM": {
            "Driver": "default",
            "Config": [
                {
                    "Subnet": "192.168.20.0/24",
                    "IPRange": "192.168.20.0/24",
                    "Gateway": "192.168.20.1"
                }
            ],
            "Options": {
                "foo": "bar"
            }
        },
        "Internal": False,
        "Attachable": False,
        "Options": {
            "com.docker.network.bridge.default_bridge": "true",
            "com.docker.network.bridge.enable_icc": "true",
            "com.docker.network.bridge.enable_ip_masquerade": "true",
            "com.docker.network.bridge.host_binding_ipv4": "0.0.0.0",
            "com.docker.network.bridge.name": "docker0",
            "com.docker.network.driver.mtu": "1500"
        },
        "Labels": {
            "com.example.some-label": "some-value",
            "com.example.some-other-label": "some-other-value"
        }
    }
    # payload = { {"Binds": ["/usr/jdy/other/:/mnt/software/"], "PortBindings": {"22/tcp": [{"HostPort": "22334"}]}}, "privileged"}
    headers = {'content-type': 'application/json'}
    url = config.dockerServer+'/networks/create'
    r = requests.post(url, data=json.dumps(networks), headers=headers)
    print('---------------- create content start --------------------')
    print(r.status_code)

    print(r.content)

    if(r.status_code == 500) :
        id = json.loads(r.content)['Id']

        print("id : " + id)
        print('---------------- create content end --------------------')


def remove():
    url = config.dockerServer + "/networks/" + id
    r = requests.delete(url)
    print('---------------- remove content start --------------------')
    print(r.status_code)

    print(r.content)

    print('---------------- remove content end --------------------')


def list():
    url = config.dockerServer + "/networks/"
    print(url)
    r = requests.get(url)
    print('---------------- remove content start --------------------')
    print(r.status_code)

    print(r.content)

    print('---------------- remove content end --------------------')


def check():
    url = config.dockerServer + "/networks/" + id
    r = requests.get(url)
    print('---------------- remove content start --------------------')
    print(r.status_code)

    print(r.content)

    print('---------------- remove content end --------------------')


create()

# remove()

# list()

# check()


## 172 network id 4500adecbab8d91fec263d0672029366a54808e69b8ae91729abff7f886e40a0

# r = requests.get("http://192.168.1.172:2375/v1.24/containers/json")
# print(r.status_code)
# print(r.content)