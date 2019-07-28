from ncclient import manager
from getpass import getpass
from pprint import pprint

#conn = manager.connect(
#    host="cisco3.lasthop.io",
#    username = "pyclass",
#    password = getpass()
#    device_params={"name": "ios_xe"},
#    hostkey_verify=False,
#    allow_agent=False,
#    look_for_keys=False,
#    port=830,
#    timeout=60,
#)

with manager.connect(
    host="cisco3.lasthop.io",
    username = "pyclass",
    password = getpass(),
    hostkey_verify=False,
    allow_agent=False,
    look_for_keys=False,
    port=830,
    timeout=60,
) as netconf_manager:

    pprint(netconf_manager.server_capabilities.__dict__)
