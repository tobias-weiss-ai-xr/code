#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import logging.handlers
import argparse
import sys
import time  # this is only being used as part of the example
import SocketServer
import rocket_cmd

# Deafults
LOG_FILENAME = "/tmp/rocket_service.log"
LOG_LEVEL = logging.DEBUG  # Could be e.g. "DEBUG" or "WARNING"

# Define and parse command line arguments
parser = argparse.ArgumentParser(description="Rocket launcher service")
parser.add_argument("-l", "--log", help="file to write log to (default '" + LOG_FILENAME + "')")

# If the log file is specified on the command line then override the default
args = parser.parse_args()
if args.log:
        LOG_FILENAME = args.log

# Configure logging to log to a file, making a new file at midnight and keeping the last 3 day's data
# Give the logger a unique name (good practice)
logger = logging.getLogger(__name__)
# Set the log level to LOG_LEVEL
logger.setLevel(LOG_LEVEL)
# Make a handler that writes to a file, making a new file at midnight and keeping 3 backups
handler = logging.handlers.TimedRotatingFileHandler(LOG_FILENAME, when="midnight", backupCount=3)
# Format each log message like this
formatter = logging.Formatter('%(asctime)s %(levelname)-8s %(message)s')
# Attach the formatter to the handler
handler.setFormatter(formatter)
# Attach the handler to the logger
logger.addHandler(handler)

# Make a class we can use to capture stdout and sterr in the log
class MyLogger(object):
        def __init__(self, logger, level):
                """Needs a logger and a logger level."""
                self.logger = logger
                self.level = level

        def write(self, message):
                # Only log if there is a message (not just a new line)
                if message.rstrip() != "":
                        self.logger.log(self.level, message.rstrip())

class TCPHandler(SocketServer.BaseRequestHandler):
    """TCP Handler for rocket launer"""
    def __init__(self, request, client_address, server):
        self.request_size= 1024
        self.step_time = 0
        self.data = 'init'
        self.mode = 'cmd'
        # python2 needs the super class on bottom and explicitly named
        SocketServer.BaseRequestHandler.__init__(self, request,
                client_address, server)

    def handle(self):
        while self.data:
            self.data = self.request.recv(self.request_size).split()
            try:
                self.command = self.data[0]
                self.step_time = self.data[1]
            except: # if data is only one word take it as command
                print('no step time given')
                self.command = self.data
            x = rocket_cmd.rocketManager() #create rocket object
            x.connect()
            x.issueCommand(self.command, self.step_time, self.mode)

class RocketServer(object):
    """Server object for network conneciton to the rocket launcher"""
    def serve(self, host, port):
        SocketServer.TCPServer.allow_reuse_address = True
        server = SocketServer.TCPServer((host, port), TCPHandler)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print('strg+c pressed')
        finally:
            server.server_close()


if __name__ == "__main__":
    # Replace stdout with logging to file at INFO level
    sys.stdout = MyLogger(logger, logging.INFO)
    # Replace stderr with logging to file at ERROR level
    sys.stderr = MyLogger(logger, logging.ERROR)

    server = RocketServer()
    server.serve('',9000)
