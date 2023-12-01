#!/bin/bash
import os
torename = []
rootdir = "./"
logfile = "./rename_log" #Eg: logfile = "/home/prasanth/renamelog"
for (path, dirs, files) in os.walk(rootdir):
    for dirname in dirs:
        if ':' in dirname:
            torename.append(os.path.join(path, dirname))
    for filename in files:
        if ':' in filename:
            torename.append(os.path.join(path, filename))

print("No of files/dirs to rename =", len(torename))
a = input("Continue? (y/n) ")
if a == 'y':
    torename.reverse()
    for oldname in torename:
        directory, filename = os.path.split(oldname)
        newname = os.path.join(directory, filename.replace(':', '-'))
        command = 'mv %s %s > /dev/null' % (repr(oldname), repr(newname))
        os.system(command)
        f = open(logfile, 'a')
        f.write(oldname + '\n')
        f.close()
else:
    print("Aborted.")
