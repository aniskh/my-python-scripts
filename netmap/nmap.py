#!/usr/bin/env python3
"""
The aim of this script is to provide functions that helps scan network.
It is can scan reachable ip addresses, open ports ...

"""
#imports
import sys
import socket
import colored

# simple function to check if a TCP/UDP port is open or noti
# ................ need recheck UDP case ..............
# without parametter, the function scan TCP ports
def check_port4(ip4,port, port_type = None):
    if port_type is None:
        port_type = 'TCP'
    # define socket type
    if port_type == 'TCP':
        port_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    elif port_type =='UDP':
        port_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #create socket
    port_socket.settimeout(1)
    check_connection = port_socket.connect_ex((ip4,port))
    #check port status
    if check_connection == 0:
        status=True
    else:
        status=False
    #close opened socket
    port_socket.close()
    return status

#function to scan all TCP/UDP ports ( default TCP )
def check_ports4(ip4,proto = None):
    if ( proto is None ) or (proto == 'TCP' ):
        file_name="tcp_ports.txt"
    elif proto == 'UDP':
        file_name="udp_ports.txt"
    ip_address = ip4
    try:
        ports_file = open(file_name, "r")
    except FileNotFoundError:
        colored.logcol("File not found, exiting program", 'err')
        sys.exit(1)
    colored.logcol("IP address:" + ip4,'warn')
    colored.logcol("Starting " + proto + " port scanning ...", 'warn')
    ports_open=[]
    for line in ports_file:
        port=int(line.split(' ')[0])
        #port=int(line)
        status = check_port4(ip_address,port,proto)
        if status :
            ports_open.append(line)
    ports_file.close()
    return ports_open
def main():
    try:
        ip_address=str(sys.argv[1])
    except IndexError:
        #print ('\033[31m red \033[37m ')
        colored.logcol("please specify the IP address", "err")
        sys.exit(1)
    proto = 'TCP'
    try:
        port_type = str(sys.argv[2])
        if port_type == 'TCP':
            proto = 'TCP'
        elif port_type == 'UDP':
            proto = 'UDP'
    except IndexError:
        pass
    ports_open = check_ports4(ip_address,proto)
    colored.logcol("Open ports found: ",'warn')
    print(*ports_open, sep = "")
    
if __name__ == "__main__":
    main()

