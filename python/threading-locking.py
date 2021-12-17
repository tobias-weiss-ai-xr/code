# Thread locking

import logging
import threading
from concurrent.futures import ThreadPoolExecutor
import time
import random

counter = 0 # global

# Test function
def test(count):
    global counter
    threadname = threading.current_thread().name
    logging.info(f'Starting: {threadname}')
    
    for x in range(count):
        logging.info(f'Count: {threadname} += {count}')
        logging.critical

        # Global interpreter lock - GIL
        # race condition
      
        # counter += 1
        
        # # locking
        # lock = threading.Lock()
        # lock.acquire()    
        # try:
        #     counter += 1
        # finally:
        #     lock.release()   
    
        # locking simplified
        lock = threading.Lock()
        with lock:
            logging.info(f'Locked: {threadname}')
            counter += 1
            time.sleep(2)
            
    logging.info(f'Completed: {threadname}')
    
def main():
    logging.basicConfig(format='%(levelname)s = %(asctime)s.%(msecs) 03d: %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)
    logging.info('App started')
    
    workers = 2
    with ThreadPoolExecutor(max_workers=workers) as ex:
        for x in range(workers*2):
            v = random.randrange(1,5)
            ex.submit(test, v)
            
    logging.info(f'{counter =}')
            
    logging.info('App finished')
    
if __name__ == "__main__":
    main()