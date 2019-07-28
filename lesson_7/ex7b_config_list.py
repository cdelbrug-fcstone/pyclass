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

config = device.config_list(["interface loopback180", "ip address 10.50.10.10/32", "interface loopback170", "ip address 10.50.20.20/32"])

for output_list in config:
    print(etree.tostring(output_list).decode())

