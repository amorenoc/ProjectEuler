#!/usr/bin/env python
def genperm(a,l):
	if len(l) == 1:
		return l
	for i,e in enumerate(l):
			a.append(genperm([e], l[:i] + l[i+1:]))
	return a

a = []
print genperm(a,[1,2,3])
