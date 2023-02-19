#!/usr/bin/env python3.8

import argparse
import os
import re
import sys
import time


# Useful for multiple ASA-5525 X and Huawei-CE12800 administration


# Argparse module for adding keys at script execution
parser = argparse.ArgumentParser()
parser.add_argument("-a", "--asa", help="Rename asa config file", action="store_true")
parser.add_argument("-c", "--huawei", help="Move and rename huawei config files", action="store_true")
args = parser.parse_args()


# If no keys added
if not len(sys.argv) > 1:
    print("No option found!")
    print("Use -h or --help key...")


'''
Check backup config for 2 ASA
Both "dir1" & "dir2" variables set path to device configs
Change name ASA_ to your in log file
'''
if args.asa:

    dir1 = "/path/to/config1/directory/"
    dir2 = "/path/to/config2/directory/"
    time_str = time.strftime("%d-%m-%Y_%H:%M:%S")
    cfg = "asa-running.cfg"

    os.chdir(dir1)
    try:
        os.rename(cfg, time_str + "_" + cfg)
    except SyntaxError:
        logfile = open('/var/log/cfg_backup.log', 'a')
        logfile.write(time_str + ": " + "ASA_1 not backup!" + "\n")
        logfile.close()

    os.chdir(dir2)
    try:
        os.rename(cfg, time_str + "_" + cfg)
    except SyntaxError:
        logfile = open('/var/log/cfg_backup.log', 'a')
        logfile.write(time_str + ": " + "ASA_2 not backup!" + "\n")
        logfile.close()


'''
In "myDir" variable set path to all config location
In "cfg" variable set name of zip file, generating by device
In "dest" variable set path to device config
'''
if args.huawei:

    myDir = "/var/lib/tftpboot/"
    time_str = time.strftime("%d-%m-%Y_%H:%M:%S")

    cfg = ["huawei1.zip", "huawei2.zip", "vrpcfg.zip"]
    dest = ["path/to/device1/directory/", "path/to/device2/directory/", "path/to/device3/directory/"]

    os.chdir(myDir)

    try:
        files = next(os.walk(myDir))[2]
        cfg_exist = [os.path.exists(myDir + cfg[0]), os.path.exists(myDir + cfg[1]), os.path.exists(myDir + cfg[2])]
        if cfg_exist:
            os.rename(myDir+cfg[0], myDir + dest[0] + time_str + "_" + cfg[0])
            os.rename(myDir+cfg[1], myDir + dest[1] + time_str + "_" + cfg[1])
            os.rename(myDir+cfg[2], myDir + dest[2] + time_str + "_" + cfg[2])
            logfile = open('/var/log/cfg_backup.log', 'a')
            logfile.write(time_str + ": " + "Configs backup!" + "\n")
            logfile.close()
    except SyntaxError:
        files = next(os.walk(myDir))[2]
        logfile = open('/var/log/cfg_backup.log', 'a')
        logfile.write(time_str + ": " + "These configs backup: " + ', '.join(files) + "\n")
        logfile.close()
