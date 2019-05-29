from ciscoconfparse import CiscoConfParse
from netmiko import ConnectHandler
from pprint import pprint

filename = "bgp_output.txt"

parsed_bgp = CiscoConfParse(filename)

neighbors = parsed_bgp.find_objects_w_child(parentspec=r"^\s+neighbor", childspec=r"\s+remote-as")

bgp_peers = []

for neighbor in neighbors:
  # neighbor IP is the first thing in the list (print the ciscoconfparse text and sepearate it with a space?)
  neighbor_ip = neighbor.text.split()
  for child in neighbor.children:
    if "remote-as" in child.text:
      _, remote_as = child.text.split()
  bgp_peers.append((neighbor_ip, remote_as))

print()
print("BGP Peers: ")
pprint(bgp_peers)
print()
