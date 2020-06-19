#!/usr/bin/env python3
"""
The aim of this script is to scan local network and list connected devices

"""
#imports
import colored
import socket

def my_ipaddresses():
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)

