#!/usr/bin/env python

numbers = {
	1: "one",
	2: "two",
	3: "three",
	4: "four",
	5: "five",
	6: "six",
	7: "seven",
	8: "eight",
	9: "nine",
	10: "ten",
	11: "eleven",
	12: "twelve",
	13: "thirteen",
	14: "fourteen",
	15: "fifteen",
	16: "sixteen",
	17: "seventeen",
	18: "eighteen",
	19: "nineteen",
	20: "twenty",
	30: "thirty",
	40: "forty",
	50: "fifty",
	60: "sixty",
	70: "seventy",
	80: "eighty",
	90: "ninety",
	100: "hundred",
	1000: "thousand"
}

def speller(x):
	global numbers
	result = 0
	if x in numbers:
		result += len(numbers[x])
		if x == 100 or x == 1000:
			result += len(numbers[1])
			print numbers[1]
		print numbers[x]
	else:
		while x > 0:
			m = 1
			for l in range(len(str(x))-1):
				m *= 10
			if x in numbers:
				result += len(numbers[x])
				print numbers[x]
				break
			elif x - x%m in  numbers:
				result += len(numbers[x-x%m])
				print numbers[x-x%m]
			else:
				result += (len(numbers[x//m]) + len(numbers[m]))
				print numbers[x//m],numbers[m]
			if m == 100 or m == 1000:
				if x % m != 0:
					result += 3 # 'and'
					print "and"
				if x // m == 1:
					result += len(numbers[1])
					print "one"
			x = x%m
	return result


def p17(n):
	global numbers
	result = 0
	for x in xrange(1,n+1):
		print x
		result += speller(x)
	return result

print p17(1000)
