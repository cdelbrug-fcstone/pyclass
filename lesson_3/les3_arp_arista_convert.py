import json
from pprint import pprint

filename = "json_arp_arista.json"

with open(filename) as f:
    arp_data = json.load(f)

arp_dict = {}
# extract a layer which includes all info - ip, mac, interface, age
arp_entries = arp_data["ipV4Neighbors"]

for entry in arp_entries:
    # store ip address from extracting the "address" key
    ip_addr = entry["address"]
    # store mac address from extracting the "hwAddress" key
    mac_addr = entry["hwAddress"]
    # add to dictionary, ip_addr key with the value being the mac_addr 
    arp_dict[ip_addr] = mac_addr

print()
pprint(arp_dict)
print()
