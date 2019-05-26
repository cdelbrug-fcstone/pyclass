from netmiko import ConnectHandler
import time
from getpass import getpass

password = getpass()

cisco4 = {

    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_ios",
    "secret": "88newclass",
    "session_log": "my_output.txt",
}

connection = ConnectHandler(**cisco4)

print(connection.find_prompt())

connection.config_mode()

print(connection.find_prompt())

connection.exit_config_mode()

print(connection.find_prompt())

connection.write_channel("disable\n")
time.sleep(2)

print(connection.read_channel())

connection.enable()

print(connection.find_prompt())

