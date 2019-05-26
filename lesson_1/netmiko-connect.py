from netmiko import ConnectHandler
from getpass import getpass

password = getpass()

nxos1 = {
    'device_type': 'cisco_nxos',
    'host': 'nxos1.lasthop.io',
    'username': 'pyclass',
    'password': password,
    }

nxos2 = {
    'device_type': 'cisco_nxos',
    'host': 'nxos2.lasthop.io',
    'username': 'pyclass',
    'password': password,
    }

for connect in nxos1, nxos2:
    net_conn = ConnectHandler(**connect)
    print(net_conn.find_prompt())

# net_connect = ConnectHandler(**nxos1)

