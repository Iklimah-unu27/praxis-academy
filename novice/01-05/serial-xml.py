from bs4 import BeautifulSoup

with open('01-05/coba.xml','r') as warno:
	warni= warno.read()

werni = BeautifulSoup(warni, 'xml')
print(warni)
