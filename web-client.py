#!/usr/bin/python3
#web-client.py

import requests

url = "http://192.168.204.68:8080/index.html"
response = requests.get(url)

flag=""

for i in range(1,51):
    url = f"http://192.168.204.68:8080/{i}.html"
    print(url)
    response = requests.get(url)
    flag+=response.text
    print(response.text)
# print(response.content.decode())
# print(response.status_code)
# print(response.headers)
print(flag.replace(" ", ""))
