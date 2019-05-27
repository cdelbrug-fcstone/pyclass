import yaml
from netmiko import ConnectHandler

filename = ".netmiko.yml"

with open(filename) as f:
    device_list = yaml.load(f)

net_connect = ConnectHandler(**device_list['cisco3'])

print(net_connect.find_prompt())
