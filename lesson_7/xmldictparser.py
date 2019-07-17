import xmltodict
from pprint import pprint

def xmldictparser(filename):
    with open(f"{filename}") as f:
        xml_file = f.read()

    return xmltodict.parse(xml_file)
