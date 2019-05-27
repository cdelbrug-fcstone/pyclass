import re
from pprint import pprint

arp_data = """
Protocol  Address      Age  Hardware Addr   Type  Interface
Internet  10.220.88.1   67  0062.ec29.70fe  ARPA  Gi0/0/0
Internet  10.220.88.20  29  c89c.1dea.0eb6  ARPA  Gi0/0/0
Internet  10.220.88.22   -  a093.5141.b780  ARPA  Gi0/0/0
Internet  10.220.88.37 104  0001.00ff.0001  ARPA  Gi0/0/0
Internet  10.220.88.38 161  0002.00ff.0001  ARPA  Gi0/0/0
"""

#strip the new line /n at the beginning and end of the text
arp_data = arp_data.strip()
#convert into a list, with the separator being a ' '
arp_list = arp_data.splitlines()

#create a blank list
processed_list = []
for arp_entry in arp_list:
    #if at the beginning at the line you see Protocol, followed by any character except line break, one or more times, and Interface inside of arp_entry, then continue
    if re.search(r"^Protocol.*Interface", arp_entry):
        continue
    #throw away Protocol, Age, and Type, store others, and then split each entry into a list with the default separator of ' '
    _, ip_addr, _, mac_addr, _, intf = arp_entry.split()
    #create a dictionary with the variables above
    arp_dict = {"mac_addr": mac_addr, "ip_addr": ip_addr, "interface": intf}
    processed_list.append(arp_dict)

print()
pprint(processed_list)
print()
