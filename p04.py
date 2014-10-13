#!/usr/bin/env python

# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

from math import sqrt

def isPalindrome(x):
    l = []
    while x:
        l.append(x % 10)
        x = x // 10
    if l == l[::-1]:
        return True
    return False

def largestPalindrome(number):
    l = []
    while number > sqrt(number):
        for i in reversed(range(2,1000)):
            y = number * i
            if isPalindrome(y):
                #print x, "x", i, "=", y
                l.append(y)
        number -= 1
    return max(l)

print largestPalindrome(999)
