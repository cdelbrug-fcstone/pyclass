from getpass import getpass
from jnpr.junos import Device
from pprint import pprint
from jnpr_devices import srx2

device = Device(**srx2)

device.open()
pprint(device.facts)
print()
print(f"Hostname: {device.facts['hostname']}")
print()
device.close()

