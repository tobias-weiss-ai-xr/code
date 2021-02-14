# setup.py that excludes installing the "tests" package

import pytest
from rocket import rocket_facedetect

@pytest.mark.default
def test_facedetect_object():
    facedetect = rocket_facedetect.rocketFacedetect()
    facedetect.capture()

