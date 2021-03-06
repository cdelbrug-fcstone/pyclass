import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from getpass import getpass
from nxapi_plumbing import Device
from lxml import etree

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

password = getpass()

device = Device(
    api_format="xml",
    host="nxos1.lasthop.io",
    username="pyclass",
    password=password,
    transport="https",
    port=8443,
    verify=False,
    )

output = device.show("show interface Ethernet1/1")


#print(etree.tostring(output).decode()) 
#print(output.find(".//{*}state").text)

intf_name = output.find(".//{*}interface").text
intf_state = output.find(".//{*}state").text
intf_mtu = output.find(".//{*}eth_mtu").text


print(f"Interface: {intf_name}; State: {intf_state}; MTU: {intf_mtu}")
