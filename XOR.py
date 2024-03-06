#!/usr/bin/python3
from itertools import cycle

key = 'K'
message = 'text to encrypt'

cryptedMessage = ''.join(chr(ord(c)^ord(k)) for c,k in zip(message, cycle(key)))

print(cryptedMessage)
print(cryptedMessage.encode())

decrypt = '153528n904o13716n8oo0r11693q9768n2sp8n7p38q879opp930s707013rss03'

plaintext = ''.join(chr(ord(c)^ord(k)) for c,k in zip( decrypt, cycle(key)))

print(plaintext)
