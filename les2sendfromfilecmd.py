from netmiko import ConnectHandler
from getpass import getpass

password = getpass()

nxos1 = {

    "host": "nxos1.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_nxos",
}

nxos2 = {

    "host": "nxos2.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_nxos",
}

nxos1_conn = ConnectHandler(**nxos1)
nxos2_conn = ConnectHandler(**nxos2)

output = nxos1_conn.send_config_from_file("les2_sendfromfile.txt")
output += nxos1_conn.save_config()
output += nxos2_conn.send_config_from_file("les2_sendfromfile.txt")
output += nxos2_conn.save_config()

print(output)
