from netmiko import ConnectHandler
from datetime import datetime
from getpass import getpass

cisco3 = {

    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_ios",
}

connection = ConnectHandler(**cisco3)

config = connection.send_config_set(["ip name-server 1.1.1.1", "ip name-server 1.0.0.1", "ip domain-lookup"])

print(config)
