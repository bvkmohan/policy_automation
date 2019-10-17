import re


def slash_to_mask(self, slash):

    slash = str(slash)
    if slash[0] == "3":
        if slash[1] == "2":
            return "255.255.255.255"
        if slash[1] == "1":
            return "255.255.255.254"
        if slash[1] == "0":
            return "255.255.255.252"
    if slash[0] == "2":
        if slash[1] == "9":
            return "255.255.255.248"
        if slash[1] == "8":
            return "255.255.255.240"
        if slash[1] == "7":
            return "255.255.255.224"
        if slash[1] == "6":
            return "255.255.255.192"
        if slash[1] == "5":
            return "255.255.255.128"
        if slash[1] == "4":
            return "255.255.255.0"
        if slash[1] == "3":
            return "255.255.254.0"
        if slash[1] == "2":
            return "255.255.252.0"
        if slash[1] == "1":
            return "255.255.248.0"
        if slash[1] == "0":
            return "255.255.240.0"
    if slash[0] == "1":
        if slash[1] == "9":
            return "255.255.224.0"
        if slash[1] == "8":
            return "255.255.192.0"
        if slash[1] == "7":
            return "255.255.128.0"
        if slash[1] == "6":
            return "255.255.0.0"
        if slash[1] == "5":
            return "255.254.0.0"
        if slash[1] == "4":
            return "255.252.0.0"
        if slash[1] == "3":
            return "255.248.0.0"
        if slash[1] == "2":
            return "255.240.0.0"
        if slash[1] == "1":
            return "255.224.0.0"
        if slash[1] == "0":
            return "255.192.0.0"
    if slash == "9":
        return "255.128.0.0"
    if slash == "8":
        return "255.0.0.0"
    if slash == "7":
        return "254.0.0.0"
    if slash == "6":
        return "252.0.0.0"
    if slash == "5":
        return "248.0.0.0"
    if slash == "4":
        return "240.0.0.0"
    if slash == "3":
        return "224.0.0.0"
    if slash == "2":
        return "192.0.0.0"
    if slash == "1":
        return "128.0.0.0"
    if slash == "0":
        return "0.0.0.0"
    return None


def mask_to_slash(self, mask):

    mask = str(mask).split(".")

    if mask[0] == "255":
        if mask[1] == "255":
            if mask[2] == "255":
                if mask[3] == "255":
                    return 32
                if mask[3] == "254":
                    return 31
                if mask[3] == "252":
                    return 30
                if mask[3] == "248":
                    return 29
                if mask[3] == "240":
                    return 28
                if mask[3] == "224":
                    return 27
                if mask[3] == "192":
                    return 26
                if mask[3] == "128":
                    return 25
                if mask[3] == "0":
                    return 24
            if mask[2] == "254" and mask[3] == "0":
                return 23
            if mask[2] == "252" and mask[3] == "0":
                return 22
            if mask[2] == "248" and mask[3] == "0":
                return 21
            if mask[2] == "240" and mask[3] == "0":
                return 20
            if mask[2] == "224" and mask[3] == "0":
                return 19
            if mask[2] == "192" and mask[3] == "0":
                return 18
            if mask[2] == "128" and mask[3] == "0":
                return 17
            if mask[2] == "0" and mask[3] == "0":
                return 16
        if mask[1] == "254" and mask[2] == "0" and mask[3] == "0":
            return 15
        if mask[1] == "252" and mask[2] == "0" and mask[3] == "0":
            return 14
        if mask[1] == "248" and mask[2] == "0" and mask[3] == "0":
            return 13
        if mask[1] == "240" and mask[2] == "0" and mask[3] == "0":
            return 12
        if mask[1] == "224" and mask[2] == "0" and mask[3] == "0":
            return 11
        if mask[1] == "192" and mask[2] == "0" and mask[3] == "0":
            return 10
        if mask[1] == "128" and mask[2] == "0" and mask[3] == "0":
            return 9
        if mask[1] == "0" and mask[1] == "0" and mask[1] == "0":
            return 8
    if mask[0] == "254" and mask[1] == "0" and mask[2] == "0" and mask[3] == "0":
        return 7
    if mask[0] == "252" and mask[1] == "0" and mask[2] == "0" and mask[3] == "0":
        return 6
    if mask[0] == "248" and mask[1] == "0" and mask[2] == "0" and mask[3] == "0":
        return 5
    if mask[0] == "240" and mask[1] == "0" and mask[2] == "0" and mask[3] == "0":
        return 4
    if mask[0] == "224" and mask[1] == "0" and mask[2] == "0" and mask[3] == "0":
        return 3
    if mask[0] == "192" and mask[1] == "0" and mask[2] == "0" and mask[3] == "0":
        return 2
    if mask[0] == "128" and mask[1] == "0" and mask[2] == "0" and mask[3] == "0":
        return 1
    if mask[0] == "0" and mask[1] == "0" and mask[2] == "0" and mask[3] == "0":
        return 0


def get_count(self, slash):
    pass
