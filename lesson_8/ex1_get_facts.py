from getpass import getpass
from jnpr.junos import Device
from pprint import pprint

device = Device(
    host="srx2.lasthop.io", user="pyclass", passwd=getpass()
    )

device.open()
pprint(device.facts)
print()
print(f"Hostname: {device.facts['hostname']}")
print()
device.close()
