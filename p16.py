#!/usr/bin/env python

# 2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2**1000?

# NOTE: we don't need to actually do bignum ourselves: http://www.python.org/dev/peps/pep-0237
# it is just a learning exercise

def p16():
    a = []
    a.append(1)
    for i in range(1000):
        k = 0
        for i in range(len(a)):
            r = (2*a[i]+k) % 10
            if r < a[i]+k:
                if len(a) == i+1:
                    a.append(1)
                else:
                    k = 1
            else:
                k = 0
            a[i] = r
    return sum(a)

print p16()

