#!/usr/bin/env python
# -*- coding: utf-8 -*-

import SocketServer
import rocket_cmd
import os
import logging
try:
    import ConfigParser as configparser
except ImportError:
    import configparser

class TCPHandler(SocketServer.BaseRequestHandler):
    """TCP Handler for rocket launer"""
    def __init__(self, request, client_address, server):
        self.request_size= 1024
        self.step_time = 0
        self.mode = 'cmd'
        # python2 needs the super class on bottom and explicitly named
        SocketServer.BaseRequestHandler.__init__(self, request,
                client_address, server)

    def handle(self):
        self.data = self.request.recv(self.request_size).split()
        try:
            self.command = self.data[0]
            self.step_time = int(self.data[1])
        except: # if data is only one word take it as command
            logging.debug('no step time given')
            self.command = self.data
        self.gun = rocket_cmd.rocketManager() #create rocket object
        self.gun.connect()
        self.gun.move(self.command, self.step_time, self.mode)

class RocketServer(object):
    """Server object for network conneciton to the rocket launcher"""
    def __init__(self):
        #  read config
        config = configparser.ConfigParser()
        config.read(os.path.abspath(os.path.dirname(__file__))  + '/../data/defaults.cfg')
        self.host = config.get('server','host')
        self.port = int(config.get('server','port'))

    def serve(self):
        SocketServer.TCPServer.allow_reuse_address = True
        self.server = SocketServer.TCPServer((self.host, self.port), TCPHandler)
        try:
            self.server.serve_forever()
        except:
            logging.debug('server interrupted')
        finally:
            self.server.server_close()

if __name__ == "__main__":
    logging.basicConfig(level=logging.ERROR)
    server = RocketServer()
    server.serve()
