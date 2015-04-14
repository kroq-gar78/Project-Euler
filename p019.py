#!/usr/bin/env python

# Project Euler: problem 19

# How many Sundays fell on the first of the month during the twentieth
# century (1 Jan 1901 to 31 Dec 2000)?

if(__name__ == "__main__"):
	days_month = [31,28,31,30,31,30,31,31,30,31,30,31]
	print len(days_month)
	leapyear_days_month = days_month
	leapyear_days_month[1] = 29
	year = 00 # year = <the year> - 1900
	month = 0 # where January = 0
	day = 0 # 0-indexed
	dayofweek = 0 # sunday = 0
	sundays_on_first = 0
	for i in xrange(101): # do (x) years
		days_in_year = 365
		if(i>0 and (i+1900)%4==0): days_in_year = 366 # check if leap year
		list_to_use = days_month
		if(days_in_year == 366): list_to_use = leapyear_days_month
		for i in xrange(days_in_year):
			day += 1
			if(day == list_to_use[month]): # if day cap reached
				month += 1
				day = 0
				if(month == 12): # if month cap reached
					year += 1
					month = 0
			dayofweek = (dayofweek+1)%7 # bump day of week
			if year >= 1 and day == 0 and dayofweek == 0:
				sundays_on_first += 1
	print sundays_on_first
		
