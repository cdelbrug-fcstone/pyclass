import time
import re

from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

from netmiko import ConnectHandler
from my_devices import nxos1, nxos2

if __name__ == "__main__":
    env = Environment(undefined=StrictUndefined)
    env.loader = FileSystemLoader(".")

    template_file = "ex2b_template.j2"
    interface = "Ethernet1/3"

    nxos1_vars = {

        "device_name": "nxos1",
        "local_as": 22,
        "interface": interface,
        "ipv4_address": "10.240.10.1",
        "ipv4_mask": "30",
    }

    nxos2_vars = {

    "device_name": "nxos2",
    "local_as": 22,
    "interface": interface,
    "ipv4_address": "10.240.10.2",
    "ipv4_mask": "30",
    }

nxos1_vars["peer_ip"] = nxos2_vars["ipv4_address"]
nxos2_vars["peer_ip"] = nxos1_vars["ipv4_address"]

# add jinja2 vars to be included in the netmiko device dict
nxos1["j2_vars"] = nxos1_vars
nxos2["j2_vars"] = nxos2_vars  

print()
for device in (nxos1, nxos2):
    # create a copy as I AM GOING TO MODIFY THIS DICTIONARY
    tmp_device = device.copy()
    j2_vars = tmp_device.pop("j2_vars")
    template = env.get_template(template_file)
    cfg = template.render(**j2_vars)
    device_name = device["j2_vars"]["device_name"]
    print(f" {device_name} ".center(80, "#"))
    print(f"\n>>> Template output {device_name}")
    print(cfg)
    # Strippingo ut whitespace will amke CLI cfg-output display cleaner
    cfg_lines = [cfg.strip() for cfg in cfg.splitlines()]

    # establish netmiko connection
    net_connect = ConnectHandler(**tmp_device)
    # Store the ssh connection for later (so i odnt have to recoonect)
    device["ssh_conn"] = net_connect
    print(f">>> Configuring {device_name}")
    output = net_connect.send_config_set(cfg_lines)
    print(output)
    print("\n\n")

# Give BGP enough time  to reacha estab state
sleep_time = 15
print(f"Sleeping for {sleep_time} seconds...")
time.sleep(sleep_time)

print("\n\n")
print(">>> Testing ping and BGP")
for device in (nxos1,):
    net_connect = device["ssh_conn"]
    remote_ip = device["j2_vars"]["peer_ip"]

    # Test ping!
    output = net_connect.send_command(f"ping {remote_ip}")
    print(output)
    if "64 bytes from" not in output:
        print("\nPing failed!!!")
    print("\n\n")

    #Test BGP
    bgp_verify = f"show ip bgp summary | include {remote_ip}"
    ouput = net_connect.send_command(bgp_verify)
    # retrive the state/pfxRcd field which is the last field
    bgp_pattern = r"\s+(\S+)\s*$"
    match = re.search(r"\s+(\S+)\s*$", output)
    prefix_recieved = match.group(1)
    try:
        # if this is an integer, the bgp session reached teh stablished state
        int(prefix_recieved)
        print(
            f"BGP reached the established state. Prefixes received {prefix_recieved}"
            )
    except ValueError:
        print("BGP failed to reach the establshed state")

# All done - disconnect on both devices
for device in (nxos1, nxos2):
    net_connect = device["ssh_conn"]
    net_connect.disconnect()

print("\n\n")
