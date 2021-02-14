#!/usr/bin/python

import usb.core
import time
import os
import argparse
try:
    import ConfigParser as configparser
except ImportError:
    import configparser

class rocketManager(object):
    """ Handels the USB connection for movement of the rocket launcher"""
    def __init__(self):
        #  read config
        config = configparser.ConfigParser()
        config.read(os.path.abspath(os.path.dirname(__file__))  + '/../data/defaults.cfg')
        self.moves = dict()
        for k, v in config.items('moves'): # load moves into dict
            self.moves[k] = int(v, 16)
        self.idVendor = int(config.get('device','idVendor'), 16) # set hex id
        self.idProduct = int(config.get('device','idProduct'), 16)

    def connect(self):
        # find our device
        self.dev = usb.core.find(idVendor=self.idVendor, idProduct=self.idProduct)
        if self.dev is None: # was it found?
            raise ValueError("Device {}:{} not found".format(hex(self.idVendor),hex(self.idProduct)))
        # linux kernel driver must be detached to claim usb device
        if self.dev.is_kernel_driver_active(0):
            try:
                self.dev.detach_kernel_driver(0)
            except usb.core.USBError as e:
                raise ValueError('Cannot detach kernel USB driver')
        else:
            try:
                self.dev.set_configuration()
                self.dev.reset()
            except:
                raise ValueError('Cannot set configuration to USB dev')

    def center(self):
        """ movements to center gun. max up/down 1000, l/r 5000 """
        self.move('left', 5000,'cmd')
        self.move('down', 1000,'cmd')
        self.move('right', 2500,'cmd')
        self.move('up', 500,'cmd')

    def move(self, command, step_time, mode):
        """ send usb control command to the rocketlauncher """
        if command == "shoot":
            step_time = 3000 #fixed time for shooting 3 sec
        command = self.moves[command]
        self.dev.ctrl_transfer(0x21, 0x09, 0, 0,
                [0x02,command,0x00,0x00,0x00,0x00,0x00,0x00])
        if mode == "gui":
            pass #  no need to stop since there is a release click event
        elif mode == "cmd" or mode == "button":
            time.sleep(step_time / 1000.0)
            command = self.moves["stop"]
            self.dev.ctrl_transfer(0x21, 0x09, 0, 0,
                [0x02,command,0x00,0x00,0x00,0x00,0x00,0x00])
        else:
            raise ValueError("No mode given!")

def main():
    # parse commandline arguments
    parser = argparse.ArgumentParser(prog="rocket cmd interface")
    parser.add_argument('command', help='up, down, left, right, shoot')
    parser.add_argument('step_time', type=int, default=0, help="time for action in ms.")
    parser.add_argument('--mode', default='cmd', help="cmd, gui, button")
    parser.add_argument('--init', default='no', help="center gun? (yes/no)")
    parser.add_argument('--config', default='', help="use a config file")
    args = parser.parse_args()
    # get an instance and connect
    device = rocketManager()
    connection_status = device.connect()
    # init gun if requested
    if args.init == "yes":
        device.center()
    #issue command
    device.move(args.command,args.step_time, args.mode)

#main method definition
if __name__ == "__main__":
    main()
