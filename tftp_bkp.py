#!/usr/bin/env python3.8

import argparse
import glob
import os
import re
import sys
import time


# Argparse module for adding keys at script execution
parser = argparse.ArgumentParser()
parser.add_argument("-o", "--asa_1", help="Check asa_1 backup", action="store_true")
parser.add_argument("-r", "--asa_2", help="Check asa_2 backup", action="store_true")
parser.add_argument("-s", "--switch_1", help="Check 1 switches backup", action="store_true")
parser.add_argument("-t", "--switch_2", help="Check 2 switches backup", action="store_true")
args = parser.parse_args()


path = "/var/lib/tftpboot/configs/"


# FUNCTIONS
# Check every day backup ASA configs
def check_bkp():
    for log in newest:
        t = os.stat(log)
        c = t.st_ctime
        if c < old:
            print("CRITICAL - Backup is missing!")
            sys.exit(1)
        else:
            print("OK - Backup complete.")
            sys.exit(0)


# Check every week backup Cisco & Huawei switches configs
def check_switch():
    for p in range(len(switches)):
        os.chdir(switches[p])
        now = time.time()
        old = now - (7 * 86400)
        filelist = os.listdir(os.getcwd())
        filelist = filter(lambda x: not os.path.isdir(x), filelist)
        newest = max(filelist, key=lambda x: os.stat(x).st_mtime)
        t = os.stat(newest)
        c = t.st_ctime
        if c < old:
            print("CRITICAL - Backup is missing: " + switches[p])
        else:
            print("OK - Backup complete: " + switches[p] + newest)


# If no keys added
if not len(sys.argv) > 1:
    print("No option found")
    print("Use -h or --help key...")


# If path to config file different, change "asa_1_path" value.
if args.asa_1:
    asa_1_path = "/var/lib/tftpboot/configs/ASA1/"
    os.chdir(asa_1_path)
    asa1Now = time.time()
    asaOld1 = asa1Now - 86400
    asa1Filelist = os.listdir(os.getcwd())
    asa1Filelist = filter(lambda x: not os.path.isdir(x), asa1Filelist)
    asa1Newest = max(asa1Filelist, key=lambda x: os.stat(x).st_mtime)
    check_bkp()


# If path to config file different, change "asa_2_path" value.
if args.asa_2:
    asa_2_path = "/var/lib/tftpboot/configs/ASA2/"
    os.chdir(asa_2_path)
    asa2Now = time.time()
    asaOld2 = asa2Now - 86400
    asa2Filelist = os.listdir(os.getcwd())
    asa2Filelist = filter(lambda x: not os.path.isdir(x), asa2Filelist)
    asa2Newest = max(asa2Filelist, key=lambda x: os.stat(x).st_mtime)
    check_bkp()


'''
If path to config file different, change "path" variable.
Values /switch1/, /switch2/... - directories with device names
Replace them for required.
Example: 
path = /var/lib/tftpboot/configs/Prod_1
switches = [ path + "/2960_1floor/", path + "/2960_2floor/" ]
'''
if args.switch_1:
    path = "/var/lib/tftpboot/configs/1"
    switches = [
        path + "/switch1/", path + "/switch2/", path + "/switch3/", path + "/switch4/", path + "/switch5/",
        path + "/switch6/", path + "/switch7/", path + "/switch8/", path + "/switch9/", path + "/switch10/",
        path + "/switch11/"
    ]
    check_switch()

if args.switch_2:
    path = "/var/lib/tftpboot/configs/2"
    switches = [path + "/switch1/", path + "/switch2/", path + "/switch3/", path + "/switch4/"]
    check_switch()
