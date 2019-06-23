# nxos1
# ------
# interface {{interface}}
#  ip address {{ip_address_1}}/{{netmask_1}}
# 
# nxos2
# ------
# interface {{interface}}
#  ip address {{ip_address_2}}/{{netmask_2}}

from jinja2 import FileSystemLoader
from jinja2 import Environment

env = Environment()
env.loader = FileSystemLoader(".")

iface_vars = {
    "interface": "Ethernet1/1",
    "ip_address_1": "10.1.100.1",
    "netmask_1": "24",
    "ip_address_2": "10.1.100.2",
    "netmask_2": "24",
}

template_file = "ex2_template.j2"
template = env.get_template(template_file)
config = template.render(**iface_vars)
print(config)
