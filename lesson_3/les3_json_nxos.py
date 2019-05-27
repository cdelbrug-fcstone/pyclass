import json

"""
In [8]: print(nxos_data.items())                                                                                                                                                                                                         
dict_items([('Ethernet2/1', {'ipv4': {'1.1.1.1': {'prefix_length': 24}}}), ('Ethernet2/2', {'ipv4': {'2.2.2.2': {'prefix_length': 27}, '3.3.3.3': {'prefix_length': 25}}}), ('Ethernet2/3', {'ipv4': {'4.4.4.4': {'prefix_length': 16}}, 'ipv6': {'fe80::2ec2:60ff:fe4f:feb2': {'prefix_length': 64}, '2001:db8::1': {'prefix_length': 10}}}), ('Ethernet2/4', {'ipv6': {'fe80::2ec2:60ff:fe4f:feb2': {'prefix_length': 64}, '2001:11:2233::a1': {'prefix_length': 24}, '2001:cc11:22bb:0:2ec2:60ff:fe4f:feb2': {'prefix_length': 64}}})])
"""

filename = "nxos_interfaces.json"
with open(filename) as f:
    nxos_data = json.load(f)


ipv4_list = []
ipv6_list = []

# go through first iteration which is interfaces, followed by the IP dict block. Do this through the dictionary items (key,value tuple - sequence)
for intf, ipaddr_dict in nxos_data.items():
    # go further through the dict block (ipv4 or ipv6, along with ip addr/prefix block)
    for ipv4_or_ipv6, addr_info in ipaddr_dict.items():
        # go through ip address and prefix length
        for ip_addr, prefix_dict in addr_info.items():
            # set prefix_length variable to the value of prefix_length dict key
            prefix_length = prefix_dict["prefix_length"]
            # check items in ipv4_or_ipv6 for loop for ipv4
            if ipv4_or_ipv6 == "ipv4":
                # create dictionary called ipv4_list with the ip/prefix
                ipv4_list.append(f"{ip_addr}/{prefix_length}")
            elif ipv4_or_ipv6 == "ipv6":
                ipv6_list.append(f"{ip_addr}/{prefix_length}")

print("\nIPv4 Addresses: {}\n".format(ipv4_list))
print("\nIPv6 Addresses: {}\n".format(ipv6_list))
