import pyeapi
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment
from getpass import getpass
from my_funcs import yaml_load_devices


if __name__ == "__main__":
    password = getpass()

    env = Environment(undefined=StrictUndefined)
    env.loader = FileSystemLoader(".")
    template_file = "loopback_intf.j2"

    yaml_out = yaml_load_devices("arista_devices_full.yml")
    my_devices = yaml_out["my_devices"]

    eapi_devices = []
    # going through device names (arista1, arista2)
    for device_name in my_devices:
        # adding the device yml config to the device_dict variable. example - yaml_out['arista1'] has all the paramaters
        device_dict = yaml_out[device_name]
        device_dict["password"] = password

        # gen config from templ
        # remove the 'data' string from the dictionary as we don't need it.
        j2_vars = device_dict.pop("data")
        template = env.get_template(template_file)
        cfg_lines = template.render(**j2_vars)
        # argument is not provided, all leading and trailing whitespaces are removed from the string.
        cfg_lines = cfg_lines.strip()
        # get rid of new lines, make a list separated by a space
        cfg_lines = cfg_lines.splitlines()

        # psuh config
        # create connectoin using device dictionary
        eapi_conn = pyeapi.client.connect(**device_dict)
        # create device connection node?
        device_obj = pyeapi.client.Node(eapi_conn)
        # append the dcevice object to the eapi_d4evices list above that is blank
        eapi_devices.append(device_obj)
        # store output from configuration lines pushed to the device_object
        output = device_obj.config(cfg_lines)
        print(output)

    # verify interfaces
    for device_obj in eapi_devices:
        output = device_obj.enable("show ip interface brief")
        print()
        print("-" * 50)
        print(output[0]["result"]["output"].rstrip())
        print("-" * 50)
    print()
