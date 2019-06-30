import pyeapi
from getpass import getpass
from my_funcs import yaml_load_devices

if __name__ == "__main__":
    password = getpass()


    devices = yaml_load_devices()

    for name, device_dict in devices.items():
        device_dict["password"] = password
        connection = pyeapi.client.connect(**device_dict)
        device = pyeapi.client.Node(connection)
        output = device.enable("show ip route")
        routes = output[0]["result"]["vrfs"]["default"]["routes"]

        print()
        for prefix, route_dict in routes.items():
            route_type = route_dict["routeType"]
            print()
            print(prefix)
            print("-" * 12)
            print(">" * 6, route_type)
            print(route_dict["vias"][0]["interface"])
            if route_type == "static":
                print(route_dict["vias"][0]["nexthopAddr"])
            print("-" * 12)

        print()

#[{'command': 'show ip route',
#  'encoding': 'json',
#  'result': {'vrfs': {'default': {'allRoutesProgrammedHardware': True,
#                                  'allRoutesProgrammedKernel': True,
#                                  'defaultRouteState': 'reachable',
#                                  'routes': {'0.0.0.0/0': {'directlyConnected': False,
#                                                           'hardwareProgrammed': True,
#                                                           'kernelProgrammed': True,
#                                                           'metric': 0,
#                                                           'preference': 1,
#                                                           'routeAction': 'forward',
#                                                           'routeType': 'static',
#                                                           'vias': [{'interface': 'Vlan1',
#                                                                     'nexthopAddr': '10.220.88.1'}]},
#                                             '10.220.88.0/24': {'directlyConnected': True,
#                                                                'hardwareProgrammed': True,
#                                                                'kernelProgrammed': True,
#                                                                'routeAction': 'forward',
#                                                                'routeType': 'connected',
#                                                                'vias': [{'interface': 'Vlan1'}]}},
#                                  'routingDisabled': False}}}}]
