from netmiko import ConnectHandler
from datetime import datetime

cisco4 = {

    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": "88newclass",
    "device_type": "cisco_ios",
}

connection = ConnectHandler(**cisco4)

sho_ver = connection.send_command("show version", use_textfsm=True)
show_lldp = connection.send_command("show lldp neighbors", use_textfsm=True)


print(f"""

=====================================
NEIGHBOR INTERFACE: {show_lldp[0]["neighbor_interface"]}
=====================================

""")
