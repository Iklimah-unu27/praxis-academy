import json

with open ('01-05/coba.json') as warno:
    
    warni = json.load(warno)

werni = warni['colors']

print(warni)
