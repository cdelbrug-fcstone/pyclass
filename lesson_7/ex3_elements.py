import xmltodict
from pprint import pprint
from xmldictparser import xmldictparser

file1 = xmldictparser("show_security_zones.xml")
file2 = xmldictparser("show_security_zones_trust.xml")

print(file1)
print(file2)
