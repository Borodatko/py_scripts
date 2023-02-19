#!/usr/bin/env python3.8

import socket
import time


# change only hostnames
services = {"drive.google.com": "0.0.0.0", "mail.google.com": "0.0.0.0", "google.com": "0.0.0.0"}


while 1 == 1:
    for host in services:
        ip = socket.gethostbyname(host)
        if ip != services[host]:
            print("[ERROR]", host, "IP mismatch:", services[host], ip)
        else:
            print(host, "-", ip)
        services[host] = ip
    time.sleep(1)
