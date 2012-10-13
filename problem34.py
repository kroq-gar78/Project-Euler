#!/usr/bin/env python

# Project Euler: problem 34

# Find the sum of all numbers which are equal to the sum of the
# factorial of their digits.

# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

import math

def sepDigits(n):
	digits = []
	for i in str(n):
		digits += i
	return digits

def factorialSum(digits,factorials):
	digitfactorials = digits
	for i in xrange(len(digitfactorials)):
		digitfactorials[i] = factorials[int(digits[i])]
	return sum(digitfactorials)

if(__name__ == '__main__'):
	
	# find intersection of [9]*x ('x' digits of 9) and the line 'x*9!'
	# ('x' times nine factorial)
	
	'''factorial9 = math.factorial(9)
	factorialamt = factorial9
	concatamt = "9"
	for i in xrange(10000):
		print factorialamt, int(concatamt)
		factorialamt += factorial9
		concatamt += '9'
		if(factorialamt < int(concatamt)):
			print i+1
			break'''
	
	maxdigits = 6 # output acquired from code above
	
	# precalculate all factorials of all digits 0 to 9
	factorials = [0]*10
	for i in xrange(10):
		factorials[i] = math.factorial(i)
	
	answers = []
	for i in xrange(3,10**6):
		if(factorialSum(sepDigits(i),factorials)==i):
			answers.append(i)
	print sum(answers)
