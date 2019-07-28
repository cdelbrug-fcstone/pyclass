from my_devices import dev_list 
from pprint import pprint
from my_functions import get_device
from napalm import get_network_driver

for dev_conn in dev_list:
    device = get_device(dev_conn)
    print(device)
    pprint(device.get_facts())

