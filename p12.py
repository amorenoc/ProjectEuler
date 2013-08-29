#!/usr/bin/env python

# The sequence of triangle numbers is generated by adding the natural numbers. 
# So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
# What is the value of the first triangle number to have over five hundred divisors?

import math

def sieve(x):
    a = [i for i in xrange(3,x,2)]
    sqrtx = math.sqrt(x)
    for j in range(len(a)):
        if sqrtx < a[j]:
            break
        a[:] = a[0:j+1] + [i for i in a[j+1:] if i % a[j]]
    a.insert(0,2)
    return a

def primeDivisors(a,n):
    for i in a:
        if i <= n:
            if n % i:
                continue
            else:
               yield i
        else:
            return

def getDivCount(a,x):
    div = [1]
    t = 1
    for i in primeDivisors(a,x):
        div.append(1)
        while x % (t*i) == 0:
            t *= i
            div[-1] += 1
    return reduce(lambda a,b: a*b, div)

def getTriangleDivCount(x):
    y = x+1
    a = sieve(y)
    if not a:
        return 1
    if x % 2 == 0:
        x //= 2
    else:
        y //= 2
    return getDivCount(a,x)*getDivCount(a,y)

def p12():
    x = 1
    while True:
        if getTriangleDivCount(x) > 500:
            return x*(x+1)/2
        x += 1

print p12()

