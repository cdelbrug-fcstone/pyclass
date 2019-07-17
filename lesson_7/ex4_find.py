from lxml import etree

with open("show_security_zones.xml") as f:
    xml_file = f.read()

my_xml = etree.fromstring(xml_file)

firstag = my_xml.find('zones-security')  

print(firstag.text)

for children in firstag.getchildren():
    print(children.text)

