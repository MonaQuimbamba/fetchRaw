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

def checkPaket():
    print(" only cap and not pcap")

def fetch(file,protocol,motif):
    pkts = rdpcap(file)
    for pkt in [p for p  in pkts if TCP in p]:
        if Raw in pkt:
            data = pkt[Raw]
            print(colored(data,color="white"))
if __name__ == "__main__":
    main()
    parser = argparse.ArgumentParser()
    parser.add_argument("-f","--file", help="packet captured [ex bgplu.cap] ", required=True)
    parser.add_argument('-p','--protocol' , help = 'The Protocol we want pull the data [ex : TCP]' , required=True)
    args = parser.parse_args()
    argsdict = vars(args)

    fetch(argsdict['file'],argsdict['protocol'],"")
