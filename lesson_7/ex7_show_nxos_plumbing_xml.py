import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from getpass import getpass
from nxapi_plumbing import Device

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
