#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

from https://automatetheboringstuff.com/chapter7/

"""
import re


def isPhoneNumber(arg):
    """
    Checks if a string is a phone number or not
    """
    if len(arg) != 12:
        return False
    for i in range(0, 3):
        if not arg[i].isdecimal():
            return False
    if arg[3] != '-':
        return False
    if arg[7] != '-':
        return False
    for i in range(8, 12):
        if not arg[i].isdecimal():
            return False
    return True


if __name__ == '__main__':
    print('415-555-4242 is a phone number:')
    print(isPhoneNumber('415-555-4242'))
    print('Moshi moshi is a phone number:')
    print(isPhoneNumber('Moshi moshi'))

    message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'

    for i in range(len(message)):
        chunk = message[i:i+12]
        if isPhoneNumber(chunk):
            print('Phone number found: ' + chunk)
    print('Done!')

    phoneNumeRegex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
    mo = phoneNumeRegex.search(message)
    areaCode, mainNumber = mo.groups()
    print('Phone number found: ' + mo.group())
    print('Area code: ' + areaCode + ' Main number: ' + mainNumber)
