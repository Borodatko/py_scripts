#!/usr/bin/env python3.8

import os
import time
import sys


if len(sys.argv) != 2:
    print("Usage:", sys.argv[0], "<dir>")
    print("Find & delete files older 2 weeks")
    sys.exit(1)


workdir = sys.argv[1]
now = time.time()
old = now - 14 * 24 * 60 * 60
time_str = time.strftime("%d-%m-%Y_%H:%M:%S")


for f in os.listdir(workdir):
    path = os.path.join(workdir, f)
    if os.path.isfile(path):
        stat = os.stat(path)
        if stat.st_ctime < old:
            os.remove(path)


if len(os.listdir(workdir)) > 14:
    logfile = open('/var/log/cfg_backup.log', 'a')
    logfile.write(time_str + ": " + "Old files not deleted" + "\n")
    logfile.close()
else:
    logfile = open('/var/log/cfg_backup.log', 'a')
    logfile.write(time_str + ": " + "Old files deleted" + "\n")
    logfile.close()
