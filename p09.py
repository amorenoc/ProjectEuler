#!/usr/bin/env python

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

from math import sqrt

def p9():
    a = 3

    while True:
        a += 2
        found = False
        b = 4
        while True:
            b += 4
            if b > 1000:
                break
            if a + b + sqrt(a**2 + b**2) == 1000:
                found = True
                break
        if found:
            break
    c = 1000 - b - a
    return a * b * c

print p9()
