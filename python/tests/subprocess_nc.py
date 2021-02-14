#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess

args= ['nc', 'localhost', '9000', '-v']
#args= 'nc localhost 9000 << EOF'

if __name__ == '__main__':
    print args
    x = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
    print x.pid
    ret, err = x.communicate('test')
