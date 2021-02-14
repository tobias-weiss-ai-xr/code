#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Various functions to compute the mandelbrot function

z_0 = 0
z_1 = 1
z_2 = (z_1)^2 + c
z_n+1 = (z_n)^2+c
"""
import numpy as np


def mandelbrot(z, maxiter):
    c = z
    for n in range(maxiter):
        if abs(z) > 2:
            return n
        z = z*z+c
    return maxiter


def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, maxiter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    return (r1, r2,
            [mandelbrot(complex(r, i), maxiter) for r in r1 for i in r2])


if __name__ == '__main__':
    mandelbrot_set(-2.0, 0.5, -1.25, 1.25, 1000, 1000, 80)
