import requests


r = requests.get('http://192.168.1.14:5000/clienttwo')

print(type(r))

print(r.text)