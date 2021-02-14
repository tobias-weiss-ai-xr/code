#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Get an image from an URL and show it.

Usage:
    python3 image_test.py
"""


def get_image(url, user, password):
    """Get an image from an URL.

    Args:
        url: The URL of an image.
        user: username for HTTPBasicAuth
        password: password for HTTPBasicAuth

    Returns:
        The image as Image (PIL) object.
    """
    import requests
    return requests.get(url, auth=HTTPBasicAuth(user, password))


def show_image(filename):
    """Show an image

    Args:
        filename: The filename for the Image
    """
    from PIL import Image
    img = Image.open(filename)
    img.show()


if __name__ == '__main__':
    show_image('face.png')
