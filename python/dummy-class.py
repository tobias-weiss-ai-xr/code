#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Module Docstring

Usage:
    python3 file.py <PARAM>
"""


class Dummy:
    def __init__(self, name='default'):
        self.name = name

    def ident(self):
        print(f'class: {self.name}')



if __name__ == '__main__':
    d = Dummy()
    d.ident()
    dummy = Dummy(name='Tom')
    dummy.ident()
