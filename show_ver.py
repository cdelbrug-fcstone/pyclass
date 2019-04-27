from netmiko import ConnectHandler

file = open("show_version.txt", 'w')

router1 = {
    'device_type': 'cisco_ios',
    'host': 'cisco3.lasthop.io',
    'username': 'pyclass',
    'password': '88newclass',
    }

connection = ConnectHandler(**router1)

file.write(connection.send_command('show version'))

file.close()

