import requests


r = requests.get('http://192.168.1.14:5000/mensajito')

print(type(r))

print(r.text)