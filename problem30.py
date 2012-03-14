#!/usr/bin/env python

# Project Euler
# Problem 30
# http://projecteuler.net/problem=30

# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

numbers = []
for i in xrange(2,1000000):
	string = str(i)
	value = 0
	for j in string:
		value+=int(j)**5
	if value == i: numbers.append(i)
	if i%10000==0: print i
print sum(numbers)
