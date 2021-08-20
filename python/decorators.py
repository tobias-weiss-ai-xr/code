#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Decorators
# wrap one function around another...

# #  wrong way as test_decorator does not return anything
# def test_decorator(func):
#     print('before')
#     func()
#     print('after')
#
# @test_decorator
# def do_stuff():
#     print('Doing stuff')

# real decorator
def makeBold(func):
    def inner():
        print('before')
        func()
        print('after')
    return inner

@makeBold
def printName():
     print('Tobias')

printName()

# passing parameters to functions
