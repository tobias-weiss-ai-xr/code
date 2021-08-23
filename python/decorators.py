#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Decorators
# wrap one function around another...

# #  wrong way as test_decorator does not return anything
# def test_decorator(func):
#     print('before')
#     func()
#     print('after'
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

def numcheck(func):
    def checkInt(o):
        if isinstance(o, int):
            if o == 0:
                print('Can not divide by Zero')
                return False
            return True
        print(f'{o} is not a number')
        return False

    def inner(x, y):
        if not checkInt(x) or not checkInt(y):
            return
        return func(x, y)

    return inner
           
@numcheck
def divide(a, b):
    print(a / b)

divide(100, 3)
divide(100, 0)
divide(100, 'cat')