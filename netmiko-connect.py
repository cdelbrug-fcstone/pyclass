from netmiko import ConnectHandler

nxos1 = {
    'device_type': 'cisco_nxos',
    'host': 'nxos1.lasthop.io',
    'username': 'pyclass',
    'password': '88newclass',
    }

nxos2 = {
    'device_type': 'cisco_nxos',
    'host': 'nxos2.lasthop.io',
    'username': 'pyclass',
    'password': '88newclass',
    }

for connect in nxos1, nxos2:
    net_conn = ConnectHandler(**connect)
    print(net_conn.find_prompt())

# net_connect = ConnectHandler(**nxos1)

