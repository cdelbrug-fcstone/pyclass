from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader(".")

interface = "Ethernet1/3"

nxos1 = {
    "device_name": "nxos1",
    "local_as": 22,
    "interface": interface,
    "ipv4_address": "10.240.10.1",
    "ipv4_mask": 30,
}

nxos2 = {
    "device_name": "nxos2",
    "local_as": 22,
    "interface": interface,
    "ipv4_address": "10.240.10.2",
    "ipv4_mask": 30,
}

nxos1["peer_ip"] = nxos2["ipv4_address"]
nxos2["peer_ip"] = nxos1["ipv4_address"]

print()
for device in (nxos1, nxos2):
    print(f" {device['device_name']} ".center(80, "#"))
    template_file = "ex2b_template.j2"
    template = env.get_template(template_file)
    output = template.render(**device)
    print(output)
    print()
