#!/usr/bin/python3
#parse-beautiful.py

import urllib3
from urllib.request import urlopen
from bs4 import BeautifulSoup

mainUrl="http://192.168.204.68:8080/basic-post"

url = urlopen(mainUrl+"table")

page = url.read()
soup = BeautifulSoup(page, features="html.parser")

print(page)
# flag = ""
# #parse table in page
# for elmnt in soup.find_all("td"):
#     linkStr = str(elmnt)
#     linkStr = linkStr.split('>')[1][0]
#     flag+=linkStr
#     # url=urlopen(mainUrl+linkStr)
#     # page = url.read()
#     # soup = BeautifulSoup(page, features="html.parser")
#     print(linkStr)
# print(flag)
#parse links in page
# for elmnt in soup.find_all("a"):
#     linkStr = str(elmnt)
#     linkStr = linkStr.split('"')[1]
#     url=urlopen(mainUrl+linkStr)
#     page = url.read()
#     soup = BeautifulSoup(page, features="html.parser")
#     print(page)

