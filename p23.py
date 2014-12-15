#!/usr/bin/env python
from math import sqrt

def divisors(n):
	m = 2
	if n < 2:
		yield 0
	else:
		yield 1
	while m <= sqrt(n):
		if n % m == 0:
			yield n / m
			yield m 
		m += 1


def abundant():
	limit = 28123



if n < sum(set(divisors(n)))
