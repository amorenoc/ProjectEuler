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
			yield m 
			yield n / m
		m += 1

def amicable(x):
	num = 0
	while num < x:
		div = sum(set(divisors(num)))
		if num != div and num == sum(set(divisors(div))):
			yield num
		num += 1

print sum(amicable(10000))

