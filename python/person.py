#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Person:
    # weak private
        _name = 'No name'

    def setName(self, name):
        self._name = name
        print(f'{self._name}')

    # strong private
    def __think(self):
        print('Thinking to myself')

    def work(self):
        self.__think()

    def __init__(self):
        print('Constructor')

    def __call__(self):
        print('call someone')

class Child(Person):
    def testDouble(self):
        self.__think()
