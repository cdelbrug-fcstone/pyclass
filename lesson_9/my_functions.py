from napalm import get_network_driver

def get_device(name):
    device_type = name.pop("device_type")
    driver = get_network_driver(device_type)
    device = driver(**name)
    device.open()
    return device

def create_backup(conn_obj):
     with open(f"{conn_obj.hostname.split('.lasthop.io')[0]}.txt", "w") as f:
        f.write(conn_obj.get_config()['running'])

def create_checkpoint(conn_obj):
    with open(f"{conn_obj.hostname.split('.lasthop.io')[0]}-checkpoint_file.txt", "w") as f:
        f.write(conn_obj._get_checkpoint_file())
