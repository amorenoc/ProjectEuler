#!/usr/bin/env python

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10001st prime number?

from math import sqrt

def p7(x):
    a = [2,3]
    num = 3
    while len(a) < x:
        num += 2
        sqrtnum = sqrt(num)
        prime = True
        for i in a[1:]:
            if i > sqrtnum:
                break
            if num % i == 0:
                prime = False
                break
        if prime:
            a.append(num)
    return a[-1]

print p7(10001)



