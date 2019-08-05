import os


def run(config_location):
    config = open(config_location)
    for line in config:
        print(" > " + line.replace("\n", ""))

