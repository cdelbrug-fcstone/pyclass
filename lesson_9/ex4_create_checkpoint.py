from my_devices import nxos1
from my_functions import get_device, create_checkpoint


device = get_device(nxos1)

create_checkpoint(device)
