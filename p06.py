#!/usr/bin/env python

# The difference between the sum of the squares of the first ten natural
# numbers and the square of the sum is 3025 - 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred 
# natural numbers and the square of the sum.

def p6(x):
    a,b = [],[]
    for i in xrange(1,x+1):
        a.append(i)
        b.append(i**2)
    return sum(a)**2 - sum(b)

print p6(100)

