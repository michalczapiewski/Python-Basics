from  pprint import pprint
from jnpr.junos import Devices
dev = Devices(host="172.25.11.1",user="lab",password="lab123")
dev.open()
pprint(dev.facts)
dev.close()