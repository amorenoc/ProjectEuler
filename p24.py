#!/usr/bin/env python
from math import factorial as fac

def p24(digits, num):
    result = []
    n = len(digits) - 1
    while n >= 0:
        facn = fac(n)
        idx = num / facn
        result.append(digits[idx])
        digits = digits[:idx] + digits[idx+1:]
        num %= facn
        n -= 1
    return ''.join(result)
        
print p24('0123456789', 999999)
