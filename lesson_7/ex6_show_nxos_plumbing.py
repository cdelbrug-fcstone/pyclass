import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from getpass import getpass
from nxapi_plumbing import Device

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

password = getpass()

device = Device(
    api_format="jsonrpc",
    host="nxos1.lasthop.io",
    username="pyclass",
    password=password,
    transport="https",
    port=8443,
    verify=False,
    )

output = device.show("show interface Ethernet1/1")

intf_name = output['TABLE_interface']['ROW_interface']['interface']  
intf_state = output['TABLE_interface']['ROW_interface']['state']
intf_mtu = output['TABLE_interface']['ROW_interface']['eth_mtu']


print(f"Interface: {intf_name}; State: {intf_state}; MTU: {intf_mtu}")

