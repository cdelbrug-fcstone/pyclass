from netmiko import ConnectHandler
from getpass import getpass

password = getpass()

file = open("show_version.txt", 'w')

router1 = {
    'device_type': 'cisco_ios',
    'host': 'cisco3.lasthop.io',
    'username': 'pyclass',
    'password': password,
    }

connection = ConnectHandler(**router1)

file.write(connection.send_command('show version'))

file.close()

