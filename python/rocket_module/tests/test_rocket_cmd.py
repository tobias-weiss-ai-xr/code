import subprocess
import pytest
from rocket import *

gun = rocket_cmd.rocketManager()

@pytest.mark.default
def test_connect():
    connected = gun.connect()

@pytest.mark.default
def test_external_call():
    cmd = ["python", "rocket/rocket_cmd.py", "down", "10"]
    call = subprocess.check_call(cmd)
    assert call == 0
    cmd = ["python", "rocket/rocket_cmd.py", "up", "10"]
    call = subprocess.check_call(cmd)
    assert call == 0

@pytest.mark.default
def test_moves():
    gun.move('up', 0, 'cmd')
    gun.move('up', 0, 'button')

@pytest.mark.movement
def test_center():
    gun.center()

@pytest.mark.movement
def test_movement():
    gun.move('up', 500, 'cmd')
    gun.move('down', 500, 'cmd')
    gun.move('left', 500, 'cmd')
    gun.move('right', 500, 'cmd')
    gun.move('shoot', 500, 'cmd')
