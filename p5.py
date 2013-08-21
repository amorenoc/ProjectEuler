#!/usr/bin/env python

# 2520 is the smallest number that can be divided by each of the 
# numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible 
# by all of the numbers from 1 to 20?

def primes(num):
    x = 3 
    p = [x]
    while True:
        x += 2
        if x > num:
            break
        test = True
        for i in p:
            if x % i == 0:
                test = False
                break
        if test: p.append(x)
    p.insert(0,2)
    return p

def p5(num):
    p = primes(num)
    a = [n for n in range(2,num+1) if n not in p]
    for x in reversed(a):
        t = []
        for i in p:
            if x == 1:
                break
            if x % i == 0:
                x /= i
                t.append(i)
        while x > 1:
            for i in t:
                if x % i == 0:
                    x /= i
                    p.append(i)
    return reduce(lambda x, y : x*y, p)

print p5(20)
