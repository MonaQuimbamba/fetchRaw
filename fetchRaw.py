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

def checkPaket(argsdict):
    capname = argsdict['file']
    x = re.search("\.cap$", capname)
    if x:
      return True
    else:
      custom_fig = Figlet(font='ntgreek')
      print(colored('The packet must be .cap',color="red"))


def fetch(file,protocol,type):
    if type==2:
        pkts=file
        protocol="ETHERNET"
    else:
        pkts = rdpcap(file)
        pkts =[p for p  in pkts if protocol in p]
    i=0
    for pkt in pkts:
        if Raw in pkt:
            data = pkt[Raw]
            custom_fig = Figlet(font='mini')
            print(colored(custom_fig.renderText('pkt ['+str(i)+']'),color="red"))
            print(colored(data,color="white"))
            i+=1
    if i==0:
        print(colored(" Probably there isn't data in this protocol",color="blue"))

if __name__ == "__main__":
    main()
    parser = argparse.ArgumentParser()
    parser.add_argument("-f","--file", help="packet captured [ex bgplu.cap] ", required=False)
    parser.add_argument('-p','--protocol' , help = 'The Protocol we want pull the data [ex : TCP]' , required=False)
    parser.add_argument('-e','--ethernet' , help = 'There is an ethernet trame ? [ex : "true"]' , required=False)
    args = parser.parse_args()
    argsdict = vars(args)
    if argsdict['ethernet']=="true":
        print(colored(" Paste the HexCap here and after press  Enter twice",color="white"))
        pkt_hex = Ether(import_hexcap())
        fetch(pkt_hex,argsdict['protocol'],2)
    else:
        if argsdict['file']:
            if checkPaket(argsdict):
                fetch(argsdict['file'],argsdict['protocol'],3)
