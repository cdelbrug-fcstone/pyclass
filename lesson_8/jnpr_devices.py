from getpass import getpass
from jnpr.junos import Device

username = "pyclass"

srx2 = {
    "host": "srx2.lasthop.io",
    "user": username,
    "passwd": getpass(),
}
