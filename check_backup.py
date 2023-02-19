#!/usr/bin/env python3.8

import glob
import os
import sys
import time
import datetime


path = "/path/to/DB/backup"


'''
Suppose, that path to dumps is:
Project name Directory -> Directory with DB name -> Directory with date -> DB dump.

Directories with date creates dynamically. In that case, function below with
help of glob module "passes" them by using pattern and find dump.

iglob helps to return iterators one at a time.
If return is successful, the path to dump and dump itself are displayed.
If dump is missing, the last dump displayed.
'''
def check():
    now_date = datetime.datetime.now()
    date = now_date.strftime("%Y-%m")
    day = now_date.strftime("%d")
    my_dir = glob.glob(db2 + '**/' + date, recursive=True)
    if my_dir:
        for dir in glob.iglob(db2 + '**/' + date, recursive=True):
            if dir:
                os.chdir(dir)
                file = glob.glob(day+".sql.bz2")
                if file:
                    print("OK - Backup complete:", dir, file)
                elif not file:
                    file = glob.glob(day+".sql")
                    if file:
                        print("OK - Backup complete:", dir, file)
                    else:
                        print("CRITICAL - Backup is missing:", dir, file)
                else:
                    print("CRITICAL - Backup is missing:", dir, file)
    else:
        print("CRITICAL - Directory doesn't exist!")


if len(sys.argv) != 2:
    print("No option found")
    print("Usage:", sys.argv[0], "<database>")
    print("Database arguments: database1, database2, database3")


'''
Backup every day.
There are 2 options, depending on the dump location.
For example we need to check backup of mobile-app database.
Option 1:
Supposed dump location - /opt/backup/db/mobile-app/01-01-1970_00:00:00.sql
In "if" condition set to "mobile-app" instead of "database1"
"db1" variable set to "/mobile-app/" instead of "/database1/"
'''
if sys.argv[1] == "database1":
    db1 = path+"/database1/"
    os.chdir(db1)
    now = time.time()
    old = now - 86400
    dirlist = os.listdir(os.getcwd())
    newest = max(dirlist, key=lambda x: os.stat(x).st_mtime)
    t = os.stat(newest)
    c = t.st_ctime
    if c < old:
        print("CRITICAL - Backup is missing!")
    else:
        print("OK - Backup complete: " + newest)


# Option 2:
# Supposed dump location - /opt/backup/db/mobile-app/_priv/1970-01/01.sql.bz2
# In "elif" condition set to "mobile-app" instead of "database2"
# "db2" variable set to "/mobile-app/" instead of "/database2/"
elif sys.argv[1] == "database2":
    db2 = path+"/database2/"
    check()


# Backup every week
# Same as first option on every day backup.
# Supposed dump location - /opt/backup/db/mobile-app/01-01-1970_00:00:00.sql
# In "elif" condition set to "mobile-app" instead of "database3"
# "db3" variable set to "/mobile-app/" instead of "/database3/"
elif sys.argv[1] == "database3":
    db3 = path+"/database3/"
    os.chdir(db3)
    now = time.time()
    old = now - (7 * 86400)
    filelist = os.listdir(os.getcwd())
    filelist = filter(lambda x: not os.path.isdir(x), filelist)
    newest = max(filelist, key=lambda x: os.stat(x).st_mtime)
    t = os.stat(newest)
    c = t.st_ctime
    if c < old:
        print("CRITICAL - Backup is missing!")
    else:
        print("OK - Backup complete: " + newest)


else:
    print("Wrong option")
    print("Usage:", sys.argv[0], "<database>")
    print("Database arguments: database1, database2, database3")
