#!/usr/bin/python3
#web-client2.py

import requests
import re
from bs4 import BeautifulSoup
# from itertools import permutations


url = 'http://192.168.204.68:8080/bijection/'

# info = {"index":"0"}
# params = {'index': ["0", '1', 'val3', 'val4']}
# post = requests.post(url, data = info)
# print(post.text)
# print(post.status_code)

flag=""
for i in range(0,50):
    info = {"index":i}
    post = requests.post(url, data = info)
    print(post.text)
    soup = BeautifulSoup(post.text, features="html.parser")
    current=soup.find("div").get_text("|", strip=True)
    flag+=current
    print(current)
    print(flag)



















# string="!@#%&"
# string = list(string)
# permu = permutations(string, 5)
# print(string)
# for i in list(permu):
#     password = "discourse"+str("".join(i))
#     info = {"username":"rdescartes", "password":password}
#     # print("".join(i))
#     post = requests.post(url, data = info)
#     print(post.text)
#     print(password)




# print(post)
