#!/usr/bin/env python

# 
# Project Euler
#

# Problem 6
# Find the difference between the sum of the squares of the first one
# hundred natural numbers and the square of the sum.

def sumsquares(*nums):
	ret=0
	for n in nums:
		ret=ret+n**2
	return ret
	
def squaresum(*nums):
	ret=0
	for n in nums:
		ret=ret+n
	return ret**2

if __name__ == "__main__":
	listnums=xrange(1,101) # need 101 because top end is exclusive
	#for i in listnums:
	#	print i
	print squaresum(*listnums)-sumsquares(*listnums)
