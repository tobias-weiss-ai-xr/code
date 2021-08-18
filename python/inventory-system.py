#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A simple inventory system to showcase how
classes and inheritence work in python.


see: "Most advanced Python course" video
"""
import json
from os import path

class Inventory:
    pets = {}
    def __init__(self):
        self.load()

    def add(self, key, qty):
        q = 0
        if key in self.pets:
            v = self.pets[key]
            q = v + qty
        else:
            q = qty
        self.pets[key] = q
        print(f'Added {qty} {key}: {q} total')

    def remove(self, key, qty):
        q = 0
        if key in self.pets:
            v = self.pets[key]
            q = v - qty
        if q < 0:
            q = 0
        self.pets[key] = q
        print(f'Removed {qty} {key}: {q} total')

    def display(self):
        for k, v in self.pets.items():
            print(f'{k} = {v}')

    def load(self):
        if not path.exists('inventory.txt'):
            print("Skipping loading, file not exists!")
            return
        with open('inventory.txt', 'r') as file:
            self.pets = json.load(file)
        print('Loaded inventory')

    def save(self):
        with open('inventory.txt', 'w') as file:
            json.dump(self.pets, file)
        print('Saved inventory')


if __name__ == '__main__':
    i = Inventory()
    i.add('snake', 1)
    i.add('snake', 5)
    i.remove('snake', 3)
    i.display()
    i.save()
    i.load()
