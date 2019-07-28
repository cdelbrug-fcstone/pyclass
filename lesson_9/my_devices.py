from getpass import getpass

password = getpass()
username = "pyclass"

cisco3 = dict(
    hostname="cisco3.lasthop.io",
    device_type="ios",
    username=username,
    password=password,
    optional_args={},
    )  

arista1 = dict(
    hostname="arista1.lasthop.io",
    username=username,
    password=password,
    device_type="eos",
    optional_args={},
)

nxos1 = dict(
    hostname="nxos1.lasthop.io",
    username=username,
    password=password,
    device_type="nxos",
    optional_args={"port": 8443},
    )

dev_list = [cisco3, arista1, nxos1]

#def get_device(name):
#    dev_list = [arista1, cisco3]
#    device_type = name.pop("device_type")
#    driver = get_network_driver(device_type)
#    device = driver(**name)
#    device.open()

