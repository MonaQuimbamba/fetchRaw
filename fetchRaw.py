#!/usr/bin/python3

from scapy.all import *
from pyfiglet import Figlet
from termcolor import colored

import re
import argparse
import os
import sys
import time
import pyfiglet


def main():
    if os.name == 'nt':
        os.system('cls')

    custom_fig = Figlet(font='puffy')

    banner = """\u001b[36m
    #########__author__ = 'Claudio Antonio'
    ##########__copyright__ = 'Copyright 2021 Claudio Antonio'
    #########__version__ = '0.1'
    ########__GitHub___='https://github.com/MonaQuimbamba/fetchRaw/'
    """
    print(colored(custom_fig.renderText('fetchRaw'),color="blue"))
    print(banner)


def fetch():
    pkts = rdpcap("ch1.pcap")
if __name__ == "__main__":
    main()
    fetch()
