import xmltodict
from pprint import pprint

def xmldictparserv2(filename, force_list_char):
    with open(f"{filename}") as f:
        xml_file = f.read()

    return xmltodict.parse(xml_file, force_list={f'{force_list_char}'})

