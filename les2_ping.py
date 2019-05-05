from netmiko import ConnectHandler


cisco4 = {

    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": "88newclass",
    "device_type": "cisco_ios",
}

connection = ConnectHandler(**cisco4)

ping_cmd = "ping"
ping_ip = "8.8.8.8"

output = connection.send_command_timing(ping_cmd, strip_prompt=False, strip_command=False)
output += connection.send_command("\n", strip_prompt=False, strip_command=False, expect_string=r":")
output += connection.send_command_timing(ping_ip, strip_prompt=False, strip_command=False)
output += connection.send_command("\n", strip_prompt=False, strip_command=False, expect_string=r":")
output += connection.send_command("\n", strip_prompt=False, strip_command=False, expect_string=r":")
output += connection.send_command("\n", strip_prompt=False, strip_command=False, expect_string=r":")
output += connection.send_command("\n", strip_prompt=False, strip_command=False, expect_string=r":")
output += connection.send_command_timing("\n", strip_prompt=False, strip_command=False)

print(output)

