#!/usr/bin/env python

def p28(side):
    result = i = 1
    row = 1
    i += 1
    while i <= side*side:
        j = 1
        row += 2
        while i <= row*row:
            if j % (row-1) == 0:
                result += i
            j += 1
            i += 1
    return result

print p28(1001)




