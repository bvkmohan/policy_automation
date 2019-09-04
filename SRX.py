class SRXConfig:
    def __init__(self):
        self.hostname = None
        self.version = None
        self.interfaces = []
        self.zones = []
        self.address_book = {}
        self.address_book['global_addresses'] = None
        self.address_book['global_applications'] = None

    # 1 # INTERFACES BRANCH #

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
        self.interface_ = interface
        self.unit_ = unit
        # print(" ")
        # print(" 1> " + self.interface_ + " - " + self.unit_ + " <")
        if len(self.interfaces) > 0:
            for interface in self.interfaces:
                # print(" 2> " + interface.interface + " - " + interface.unit + " < ")
                if (
                    interface.interface == self.interface_
                    and interface.unit == self.unit_
                ):
                    # print("  RETURNING TRUE")
                    return True
            else:
                # print(" RETURNING FALSE 1 ")
                return False
        else:
            # print(" INTERFACES NOT YET ADDED")
            # print("  RETURNING FALSE 2 ")
            return False

    # 2 # SECURITY ZONES BRANCH #

    def append_zone(self, zone_name):
        self.zones.append(zone_name)

    def dump_zones(self):
        print(" ")
        for zone in self.zones:
            print(" ")
            print(" Zone Name : " + str(zone.name))
            for interface in zone.interfaces:
                print("  - " + str(interface))

    def check_zone(self, name):
        self.name_ = name
        if len(self.zones) > 0:
            for zone in self.zones:
                if zone.name == self.name_:
                    return True
            else:
                return False
        else:
            return False

    # X # ADDRESS BOOK BRANCH #

    # X.X # GLOBAL ADDRESS BOOK BRANCH

    def append_global(self):
        self.address_book["global"] = None


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

    def change_interface_status(self, status):
        if self.status is None or self.status == "enabled":
            self.status = status


class SECZone:
    def __init__(self, name):
        self.name = name
        self.interfaces = []
        # self.inbound_services = []
        # self.screens = []

    def add_interface(self, interface):
        self.interfaces.append(interface)

    # def add_inbound_service(self, service):
    # self.inbound_services.append(service)

    def check_interface(self, interface):
        self.interface_ = interface
        for intf in self.interfaces:
            if self.interface_ == intf:
                return True
        else:
            return False


class GlobalAddress:
    def __init__(self):
        self.name = "global"
        self.addresses = {}

    def add_address(self, key, value):
        self.address[key] = value

    def check_address(self, input_key):
        for key in self.address:
            if key == input_key:
                return True
        else:
            return False


srx_config = SRXConfig()


def run(config):

    for row in config:

        # 0 # SANITIZE THE CONFIGURATION FOR PARSING

        rm_nl = row.replace("\n", "")
        line = rm_nl.split(" ")

        if len(line) < 2:
            continue

        if line[1] == "groups":
            del line[1]
            del line[1]

        if len(line) < 2:
            continue

        # 1 # EXTRACT INTERFACE INFORMATION

        if line[1] == "interfaces":

            if len(line) <= 5:
                continue

            if (
                line[3] == "speed"
                or line[3] == "mtu"
                or line[3] == "link-mode"
                or line[3] == "description"
                or line[3] == "gigether-options"
                or line[3] == "fabric-options"
                or line[3] == "per-unit-scheduler"
                or line[3] == "vlan-tagging"
                or line[3] == "redundant-ether-options"
                or line[3] == "redundant-pseudo-interface-options"
                or line[3] == "no-traps"
                or line[-1] == "no-traps"
                or line[-1] == "point-to-point"
            ):
                continue

            if line[3] == "unit":
                if srx_config.check_interface(line[2], line[4]) is False:
                    if line[-1] == "disable":
                        interface = Interface(line[2], line[4], "disabled")
                        srx_config.append_interface(interface)
                        continue
                    else:
                        if line[-1] == "enable":
                            interface = Interface(line[2], line[4], "enabled")
                            srx_config.append_interface(interface)
                            continue
                        if line[6] == "inet" and line[-1] == "inet":
                            interface = Interface(line[2], line[4], "enabled")
                            srx_config.append_interface(interface)
                            continue
                        if line[6] == "inet" and line[7] == "address":
                            interface = Interface(line[2], line[4], "enabled")
                            srx_config.append_interface(interface)
                            interface.add_address_primary(line[8])
                            continue
                        else:
                            interface = Interface(line[2], line[4], "enabled")
                            srx_config.append_interface(interface)
                            continue
                else:
                    if line[-1] == "disable":
                        interface.change_interface_status("disabled")
                        continue
                    if line[-1] == "inet":
                        continue

            if line[6] == "inet" and line[7] == "filter":
                continue
            if line[6] == "inet" and line[7] == "address":
                if interface.has_address_primary() is False:
                    interface.add_address_primary(line[8])
                else:
                    if line[-1] == "primary" or line[-1] == "master-only":
                        interface.add_address_secondary(interface.get_address_primary())
                        interface.add_address_primary(line[8])
                    else:
                        interface.add_address_secondary(line[8])

        # 2 # EXTRACT ZONE INFORMATION

        if len(line) > 4 and line[1] == "security" and line[3] == "security-zone":

            if srx_config.check_zone(line[4]) is False:
                zone = SECZone(line[4])
                srx_config.append_zone(zone)
                if len(line) > 5:
                    if line[5] == "interfaces":
                        zone.add_interface(line[6])
            else:
                if len(line) > 5:
                    if line[5] == "interfaces":
                        if zone.check_interface(line[6]) is False:
                            zone.add_interface(line[6])

        # 3 # EXTRACT GLOBAL ADDRESSES INFORMATION

        if len(line) > 6 and line[2] == "address-book" and line[3] == "global":



    return srx_config
