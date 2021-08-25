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

# divide(100, 3)
# divide(100, 0)
# divide(100, 'cat')

# Decorator with unknown number of params
# We want a decorator tht can pass params and handle anything
# *args, **kwargs to the rescue

def outline(func):
    def inner(*args, **kwargs):
        print('~'*20)
        func(*args, **kwargs)
        print('~'*20)
    return inner


def list_items(func):
    def inner(*args, **kwargs):
        func(*args, **kwargs)
        print(f'args = {args}')
        print(f'kwargs = {kwargs}')
        for x in args:
            print(f'arg = {x}')
        for k, v in kwargs.items():
            print(f'key = {k}, value = {v}')
    return inner


@outline
@list_items
def display(msg):
    print(msg)

display('hello world')

@outline
@list_items
def birthday(name='', age=0):
    print(f'Happy birthday {name} you are {age} years old.')

birthday(name='brian', age=46)