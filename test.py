

import os
import socket
env = os.environ
print(env)
os.environ['ENV'] = "uat"

def test():
    import requests
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
               "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ7XCJvcmdJZFwiOlwiaGViZWl6aG9uZ3lhblwiLFwiYXBwaWRcIjpcInd4YWU4YmFhZTU2NmFhODc1OFwiLFwib3BlbmlkXCI6XCJvMVVjTTZJaVppUE9pQXktNmtVWVM5ZWV1S05nXCIsXCJ1bmlvbmlkXCI6XCJvMEhKVjBneGplN3M1MHRIdl9UWUp5clViNUpNXCIsXCJsb2dpblRpbWVcIjoxNjcwODk3OTE4MzIzLFwidGFnXCI6XCIxNjcwODk2NTQ1OTA0TDlDWjE1VThYNjFORFRaXCIsXCJ1c2VySWRcIjoxMTEzNjM2ODgzfSIsImV4cCI6MTY3MDkwMTUxOH0.7fBM3ey11M6VbK-VGLpVNrBwRZ65JAia2dabl-NaXTQ"}
    resp = requests.get('https://hbz.qrmkt.cn/syx/scan/checkResult', headers=headers)
    print(resp)
    print(resp.text)


def get_token():
    import requests
    j_data = {"url": "https://hbz.qrmkt.cn/yx/views/common/yz.html"}
    res = requests.post("https://hbz.qrmkt.cn/syx/wx/jsapi",json=j_data)
    print(res.text)

if __name__ == '__main__':
    get_token()
    test()

