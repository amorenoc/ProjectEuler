#!/usr/bin/env python

def fib(n):
	fn_1, fn_2 = 1, 1
	fi = 0
	i = 1
	while i <= n:
		if i == 1 or i == 2:
			yield 1
		else:
			fi = fn_1 + fn_2
			yield fi
			fn_2, fn_1 = fn_1, fi
		i += 1

a = [ n for n in fib(12) ]

def fibdigits(n):
	fn_1, fn_2 = 1, 1
	fi = 0
	i = 2
	while len(str(fi)) < n:
		fi = fn_1 + fn_2
		fn_2, fn_1 = fn_1, fi
		i += 1
	return i

print fibdigits(1000)
