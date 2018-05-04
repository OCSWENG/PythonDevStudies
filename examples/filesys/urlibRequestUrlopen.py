
"""
from urllib import request
import json

response = request.urlopen('http://www.python.org/')
print('RESPONSE:', response)

print('URL	:', response.geturl())

headers = response.info()
print('DATE	:', headers['date'])
print('HEADERS	:')
print('-----------')
print(headers)

data = response.read().decode('utf-8')
print('LENGTH :', len(data))
print('Data	:')
print(' ------')
print(data)
"""

import urllib.request
with urllib.request.urlopen('http://python.org/') as response:
   html = response.read()

