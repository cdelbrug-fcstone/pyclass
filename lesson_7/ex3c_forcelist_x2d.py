import xmltodict
from pprint import pprint
from xmldictparserv2 import xmldictparserv2

file1 = xmldictparserv2("show_security_zones_trust.xml", "zones-security")

print(file1)
