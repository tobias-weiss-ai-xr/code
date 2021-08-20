#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Understanding the underscore

_single, __double, __before, after_, __both__
"""
#Dummy test class
from person import Person, Child

# skipping
for _ in range(5):
    print('hello!')


p = Person()
p.setName('Brian')
# p._name = 'Nooo' #  edit weak private
# printing not even working by the lint checker
# print(f'Weak private {p._name}')

p = Person()
p.work()

# Strong private not accessable
# p.__think()

c = Child()
# c.testDouble()

# After (any)
# helps with naming conflicts with keywords...
class_ = Person()
print(class_)

p = Person()
p.__call__()
