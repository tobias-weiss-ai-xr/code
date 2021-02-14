#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Pygame basics

See https://inventwithpython.com/pygame/chapter2.html

Usage:
    python3 file.py <PARAM>
"""
import pygame
from pygame.locals import *
import sys

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello World')
while True:
    for event in pygame.event.get():
        if event.type == 'QUIT':
            pygame.quit()
            sys.exit()
    pygame.display.update()
