import json
import socket
from pprint import pprint
import SRX

settings = json.load(open("settings.json"))

if settings["run_on"] == socket.gethostname():
    config = open("test.config")
    temp_ = SRX.run(config)
    temp_.dump_address_book("networks")
