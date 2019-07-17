from lxml import etree

with open("show_version.xml", "rb") as f:
    xml_file = f.read()

my_xml = etree.fromstring(xml_file)

print(my_xml.nsmap)

print(my_xml.find(".//{*}proc_board_id").text)
