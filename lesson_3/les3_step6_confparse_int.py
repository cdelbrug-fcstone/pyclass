import yaml
from netmiko import ConnectHandler
from ciscoconfparse import CiscoConfParse

filename = "/home/cdelbrugge/.netmiko.yml"

with open(filename) as f:
    device_list = yaml.load(f)

net_connect = ConnectHandler(**device_list['cisco4'])

running_config = net_connect.send_command("show run")

parsed_running = CiscoConfParse(running_config.splitlines())

int_results = parsed_running.find_objects_w_child(parentspec=r"^interface", childspec=r"^\s+ip address")

print()
for intf in int_results:
    print(f"Interface Line: {intf.text}")
    # because its a list, specify the location
    ip_address = intf.re_search_children(r"ip address")[0].text
    print(f"IP Address Line: {ip_address}")
    print()
print()
