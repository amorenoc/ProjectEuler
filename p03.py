#!/usr/bin/env python

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

from math import sqrt

number = 600851475143

def isPrime(x):
    y = 3
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    while y < sqrt(x):
        if x % y == 0:
            return False
        y += 2
    return True

def largestPrime(x):
    y = int(sqrt(x))
    while y > 2:
        if x % y == 0:
            if isPrime(y):
                return y
        y -= 1
    return x

print largestPrime(number)


