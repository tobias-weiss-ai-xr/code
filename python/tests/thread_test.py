#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import threading
import time
import sys

class TestThread(threading.Thread):
    counter = 0
    counterLock = threading.Lock()

    def __init__(self, time):
        threading.Thread.__init__(self)
        self.daemon = True
        self.time = time

    def run(self):
        print(self.getName(), 'sleeping')
        time.sleep(self.time)
        print(self.getName(), 'finished')

if __name__ == "__main__":
    #generate thread array
    thread_list = []
    try:
        for i in range(10):
            thread_list.append('thread' + str(i))

        for t in thread_list:
            t = TestThread(10)
            t.start()

        t.join()
    except KeyboardInterrupt:
        sys.exit(0)

    while True:
        time.sleep(1)
