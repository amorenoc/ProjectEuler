#!/usr/bin/env python

def p15(n):
   """Prints out n rows of Pascal's triangle.
   It returns False for failure and True for success."""
   row = [1]
   k = [0]
   for x in range(max(n*2,0)):
      row=[l+r for l,r in zip(row+k,k+row)]
   return row[len(row)/2]

print p15(20)
