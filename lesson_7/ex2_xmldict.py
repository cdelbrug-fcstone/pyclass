import xmltodict
from pprint import pprint

with open("show_security_zones.xml") as f:
    xml_file = f.read()

parsed_xml = xmltodict.parse(xml_file)

pprint(parsed_xml)

print(type(parsed_xml))


print()
print(f"Security Zone #1: {parsed_xml['zones-information']['zones-security'][0]['zones-security-zonename']}")
print(f"Security Zone #2: {parsed_xml['zones-information']['zones-security'][1]['zones-security-zonename']}")
print(f"Security Zone #3: {parsed_xml['zones-information']['zones-security'][2]['zones-security-zonename']}")
print()

