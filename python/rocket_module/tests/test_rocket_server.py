# setup.py that excludes installing the "tests" package

import pytest
import subprocess
from rocket import rocket_server
from rocket import rocket_cmd
from multiprocessing import Process
from time import sleep

@pytest.mark.default
def test_server_object():
    server = rocket_server.RocketServer()

@pytest.mark.network
def test_tcp_with_nc():
    server = rocket_server.RocketServer("",9000)
    proc = Process(target=server.serve)
    proc.start()
    # nc via subprocess
    args = ['nc', 'localhost', '9000', '-v']
    client1 = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    ret1, err1 = client1.communicate('up 0')
    client2 = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    ret2, err2 = client2.communicate('dummy')
    proc.terminate()
    assert err1 == 'Connection to localhost 9000 port [tcp/*] succeeded!\n'
    assert err2 == 'Connection to localhost 9000 port [tcp/*] succeeded!\n'
