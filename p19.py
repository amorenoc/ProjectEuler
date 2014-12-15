#!/usr/bin/env python

sundayCount = 0

dayOfTheWeek = { 0 : 'Monday',
								 1 : 'Tuesday',
								 2 : 'Wednesday',
								 3 : 'Thursday',
								 4 : 'Friday',
								 5 : 'Saturday',
								 6 : 'Sunday'
}

def daysInMonth(year, month):
	if month in [4,6,9,11]:
		return 30
	elif month in [1,3,5,7,8,10,12]:
		return 31
	else:
		if year % 400 == 0:
			return 29
		elif year % 4 == 0 and year % 100:
			return 29
		else:
			return 28

def firstOfJanuary(start, end):
	global sundayCount
	year = 1900
	first = 0 # Monday
	month = 1
	while year < start:
		while month % 13:
			#print dayOfTheWeek[first]
			first = (first + daysInMonth(year,month)) % 7
			month += 1
		else: 
			year += 1
			month = 1
	while year < end:
		while month % 13:
			first = (first + daysInMonth(year,month)) % 7
			if first == 6:
				sundayCount += 1
			month += 1
		else: 
			year += 1
			month = 1
		
	

firstOfJanuary(1901, 2001)
print sundayCount
