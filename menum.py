#!/usr/bin/env python

from subprocess import call
import os
import sys
import datetime

with open(sys.argv[1]) as f:
    hosts = [x.strip('\n') for x in f.readlines()]

for target in hosts:
    now = datetime.datetime.now()
    os.system("enum4linux -a " + target + " > " + now.strftime("%Y-%m-%d_%H:%M:%S") + "_enum4linux_" + target)
