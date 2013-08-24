#!/usr/bin/env python

# Find the sum of the digits in the number 100!

def p20():
    x = 1
    for i in range(1,101):
        x *= i 
    y = 0
    while x > 0:
        y += x % 10
        x //= 10
    return y

print p20()
