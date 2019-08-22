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
            print(" Interface Name      : " + str(interface.interface))
            print(" Interface Unit      : " + str(interface.unit))
            print(" Interface Address 1 : " + str(interface.address_primary))
            if interface.address_secondary is not None:
                print(" Interface Address 2 : " + str(interface.address_secondary))
            print(" Interface Status    : " + str(interface.status))
            print(" ")

    def check_interface(self, interface, unit):
        print(" I GOT : " + interface + " AND " + unit)
        if len(self.interfaces) > 0:
            for interface in self.interfaces:
                if interface.interface == interface and interface.unit == unit:
                    return True
                else:
                    return False
        else:
            print(" INTERFACES NOT YET ADDED")
            return False


class Interface:
    def __init__(self, interface, unit, status):
        self.interface = interface
        self.unit = unit
        self.address_primary = None
        self.address_secondary = None
        self.status = status

    def add_address_primary(self, address):
        self.address_primary = address

    def add_address_secondary(self, address):
        self.address_secondary = address

    def has_address_primary(self):
        if self.address_primary is not None:
            return True
        else:
            return False

    def get_address_primary(self):
        return self.address_primary

    def disable_interface(self):
        if self.status is None:
            self.status = "disabled"


srx_config = SRXConfig()


def run(config):
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
            if line[3] == "description":
                continue
            if len(line) > 4 and line[-1] == "disable":
                interface = Interface(line[2], line[4], "disabled")
                srx_config.append_interface(interface)
                continue
            if len(line) > 8:
                if line[5] == "family" and line[6] == "inet" and line[7] == "address":
                    print(str(srx_config.check_interface(line[2], line[4])))
                    if srx_config.check_interface(line[2], line[4]) is False:
                        interface = Interface(line[2], line[4], "enabled")
                        interface.add_address_primary(line[8])
                        srx_config.append_interface(interface)
                        continue
                    else:
                        if interface.has_address_primary is True:
                            if line[-1] == "primary" or line[-1] == "master-only":
                                interface.add_address_secondary(
                                    interface.get_address_primary()
                                )
                                interface.add_address_primary(line[8])
                        else:
                            interface.add_address_primary(line[8])
                        continue

    return srx_config
