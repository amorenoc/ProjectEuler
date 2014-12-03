#!/usr/bin/env python
from collections import deque

result = 0
result2 = 0

def foo(side_len):
    global result
    x = deque([(0,0)])
    while len(x):
        (a,b) = x.popleft()

        if a == side_len and b == side_len:
            result += 1

        if a < side_len:
            x.append((a+1,b))

        if b < side_len:
            x.append((a,b+1))

def bar(side_len):
    global result2
    x = deque([(0,0,1)])
    while len(x):
        (a,b,c) = x.popleft()

        if a == side_len and b == side_len:
            result += 1

        if a < side_len:
            [ x[(r,s,t)] += x[(a,b,c)] for r,s,t in x if r == a+1 and s == b]
            if  x.append(a+1,b,c) 

        if b < side_len:
            if (a,b+1) in x:
                x[(a,b+1)] += x[(a,b)]
            x.append((a,b+1))

foo(3)
bar(2)

print result
