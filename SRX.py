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
            print(" Interface Status  : " + str(interface.status))
            print(" ")

    def check_interface(self, interface, unit):
        if len(self.interfaces) > 0:
            for interface in self.interfaces:
                if interface.interface == interface and interface.unit == unit:
                    return True
                else:
                    False


class Interface:
    def __init__(self, interface, unit):
        self.interface = interface
        self.unit = unit
        self.address = None
        self.status = None

    def add_interface(self, address):
        self.address = address
        self.status = "enabled"

    def disable_interface(self):
        if self.status is None:
            self.status = "disabled"  # ANCHOR


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
            if srx_config.check_interface(line)
            interface = Interface(line[2], line[4])

        if flag == "interfaces":
            if len(line) > 8:
                if line[5] == "family" and line[6] == "inet" and line[7] == "address":
                    # print(" > " + line[4] + " > " + line[8])
                    interface.add_interface(line[8])
                    srx_config.append_interface(interface)
            if (
                line[0] == "deactivate" and line[1] == "interfaces"
            ):  # DELETE LINE[1] IN FUTURE
                interface.disable_interface()
            if (
                line[-1] == "disable" and line[1] == "interfaces"
            ):  # DELETE LINE[1] IN FUTURE
                if len(line) != 4:
                    interface.disable_interface()

    return srx_config
