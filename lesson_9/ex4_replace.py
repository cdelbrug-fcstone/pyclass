from my_devices import nxos1
from my_functions import get_device, create_checkpoint
import urllib3
from pprint import pprint

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

device = get_device(nxos1)

print(">>>>>>>>>>> loading replace candidate file")
print()
device.load_replace_candidate(filename="nxos1-loopbacks.txt")
print()
print(">>>>>>> diffing config now")
print()
print(device.compare_config())
print()
print(">>>>>> cool. hopefully you saw the diff. i'm discarding it now")
pprint(device.discard_config())
print()
