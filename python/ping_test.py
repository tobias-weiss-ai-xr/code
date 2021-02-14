#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess
import os
import datetime
"""
Ping some hosts simultaniously and log if ping fails.
"""

# write results to
out_file = 'ping_fail_v2.txt'

# hosts to ping
hosts = ['heise.de', 'google.com', 'uni-jena.de', 'suse.de', 'mit.edu']

while True:
    with open(os.devnull, "wb") as limbo:
        for host in hosts:
            cmd = ["ping", "-c", "1", "-n", "-W", "2", host]
            result = subprocess.Popen(cmd, stdout=limbo, stderr=limbo).wait()
            # if result == 0:
            #     msg = host + " is up " + str(datetime.datetime.now())
            #     print(msg)
            if result != 0:
                msg = host + " is down " + str(datetime.datetime.now()) + "\n"
                print(msg)
                with open(out_file, 'a') as out_file:
                    out_file.write(msg)
