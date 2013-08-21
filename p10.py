#!/usr/bin/env python

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

from math import sqrt

def p10(x):
    a = [3]
    psum = 2
    num = 3
    if x > 3:
        psum += num
    while True:
        num += 2
        sqrtnum = sqrt(num)
        prime = True
        for i in a:
            if i > sqrtnum:
                break
            if num % i == 0:
                prime = False
                break
        if prime:
            if num > x:
                break
            psum += num
            a.append(num)
    return psum

print p10(2000000)
