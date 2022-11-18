#!/usr/bin/env python
import socket
import subprocess
import sys
from datetime import datetime

def scan(port_type, ip): 
    
    print("-" * 60)
    print("Starting", port_type, "scan...")
    print("-" * 60)

    if port_type == "TCP": 
        tcp = open("tcp.txt", "r")
        ports = tcp.read().split(",")
        tcp.close()
    else: 
        udp = open("udp.txt", "r")
        ports = udp.read().split(",")
        udp.close()

    start = datetime.now

    try: 
        for port_number in ports: 
            if port_type == "TCP":
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            else: 
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            print(port_number)
            result = sock.connect_ex((remoteServer, int(port_number)))
            if result == 0: 
                print("Port {}: 	 Open".format(port_number))
            sock.close()
    except KeyboardInterrupt:
        print("You exited the scan.")
        sys.exit()

    except socket.gaierror:
        print('Hostname could not be resolved. Exiting')
        sys.exit()

    except socket.error:
        print("Couldn't connect to server")
        sys.exit()

    end = datetime.now()
    duration = end - start

    print('Scanning Completed in: ', duration)
    print("-" * 60)

if __name__ == "__main__": 
    remoteServer = input("Enter a remote host to scan: ")
    while True: 
        tcp_scan = input("Would you like to scan TCP ports? (y/n): ")
        if tcp_scan == "y" or tcp_scan == "n": 
            break
    while True:
        udp_scan = input("Would you like to scan UDP ports? (y/n): ")
        if udp_scan == "y" or udp_scan == "n": 
            break
    
    if tcp_scan == "y":
        scan("TCP", remoteServer)
    
    if udp_scan == "y":
        scan("UDP", remoteServer)

    print("Thanks for using this tool!")