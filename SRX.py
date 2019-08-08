class SRXConfig:
    def __init__(self):
        self.hostname = None
        self.version = None
        self.interfaces = []

    def append_interface(self, interface_object):
        self.interfaces.append(interface_object)

    def dump_interfaces(self):
        print(" ")
        for interface in self.interfaces:
            print(" Interface Name    : " + str(interface.interface))
            print(" Interface Unit    : " + str(interface.unit))
            print(" Interface Address : " + str(interface.address))
            print(" ")


class Interface:
    def __init__(self):
        self.interface = None
        self.unit = None
        self.address = None

    def add_interface(self, interface, unit, address):
        self.interface = interface
        self.unit = unit
        self.address = address


srx_config = SRXConfig()


def run(config):
    flag = None
    for row in config:
        rm_nl = row.replace("\n", "")
        line = rm_nl.split(" ")

        if len(line) < 2:
            continue

        if line[1] == "groups":
            del line[1]
            del line[1]

        if len(line) < 2:
            continue

        if line[1] == "interfaces":
            flag = line[1]

        if flag == "interfaces" and len(line) > 8:
            if line[5] == "family" and line[6] == "inet" and line[7] == "address":
                interface = Interface()
                # print(" > " + line[2] + " > " + line[4] + " > " + line[8])
                interface.add_interface(line[2], line[4], line[8])
                srx_config.append_interface(interface)

    return srx_config
