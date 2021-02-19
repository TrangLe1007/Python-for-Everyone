import urllib.request, urllib.parse, urllib.error
import json

sum = 0

address = input('Enter location: ')
uh = urllib.request.urlopen(address)
data = uh.read()
info = json.loads(data)

lst = info["comments"]
for item in lst:
    sum = sum + item['count']

print(sum)
