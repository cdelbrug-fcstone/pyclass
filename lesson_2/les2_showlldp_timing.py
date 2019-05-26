from netmiko import ConnectHandler
from datetime import datetime
from getpass import getpass

password = getpass()

nxos2 = {

    "host": "nxos2.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_nxos",
    "global_delay_factor": 2,
}

connection = ConnectHandler(**nxos2)

time_before1 = datetime.now()
output = connection.send_command("show lldp neighbors detail", strip_prompt=False, strip_command=False)
time_after1 = datetime.now()

print(f"""

===========================================
          GLOBAL DELAY FACTOR
===========================================
{output}
===========================================
    """)
print(f"""
-----------------------------------------
     Time difference: {time_after1 - time_before1}
-----------------------------------------
    """)

time_before2 = datetime.now()
output2 = connection.send_command("show lldp neighbors detail", strip_prompt=False, strip_command=False, delay_factor=8)
time_after2 = datetime.now()
print(f"""

===========================================
          LOCAL DELAY FACTOR
===========================================
{output2}
===========================================
    """)
print(f"""
-------------------------------------------
     Time: {time_after2 - time_before2}
-------------------------------------------
    """)
