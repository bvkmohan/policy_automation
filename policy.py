import json
from pprint import pprint

import SRX

SRX.run("test.config")

settings = json.load(open("settings.json"))

print(settings["run_on"])

