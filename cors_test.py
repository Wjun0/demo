



import requests


session = requests.session()

header = {
    "Origin":"null",
    "Referer":"http://www.baidu.com"
}

url = "http://127.0.0.1:8080/students/"

res = session.get(url=url)
print(res)

dev = ""