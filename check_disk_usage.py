#!/usr/bin/env python3.8

import shutil
import sys


if len(sys.argv) != 2:
    print("Usage:", sys.argv[0], "<mount_point>")
    sys.exit(1)


mount_point = sys.argv[1]


usage = shutil.disk_usage(mount_point)
free_space = usage[2]
print(free_space)
