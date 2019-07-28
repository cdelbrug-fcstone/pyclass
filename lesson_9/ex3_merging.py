from my_devices import dev_list 
from pprint import pprint
from my_functions import get_device, create_backup
from napalm import get_network_driver

# excercise 3a
for dev_conn in dev_list:
    device = get_device(dev_conn)
    # exercise 3c
    print()
    print(f">>>>>>>>>> Loading merge candidate - {device.hostname}")
    print()
    device.load_merge_candidate(f"{device.hostname}-loopbacks")
    print()
    print(f">>>>>>>>>> Comparing config - {device.hostname}")
    print()
    pprint(device.compare_config())
    print()
    print(f">>>>>>>>>> Committing config - {device.hostname}")
    print()
    device.commit_config()
    print()
    print(f">>>>>>>>>> Comparing config...again - {device.hostname}")
    print()
    pprint(device.compare_config())
    print()
    print("=" * 50)


