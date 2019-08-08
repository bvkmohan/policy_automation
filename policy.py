import json
import socket
from pprint import pprint
import SRX

settings = json.load(open("settings.json"))

if settings["run_on"] == socket.gethostname():
    config = open("test.config")
    SRX.run(config)
