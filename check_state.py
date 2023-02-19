#!/usr/bin/env python3.8

import os

print("Enter path: ")
path = input()
if path[-1] != "/":
    path = path + "/"
bash_command = ["cd" + " " + path, "git status"]
result_os = os.popen(' && '.join(bash_command)).read()

for result in result_os.split('\n'):
    if result.find('modified') != -1:
        prepare_result = result.replace('\tmodified:   ', path)
        print(prepare_result)
