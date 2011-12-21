#!/usr/bin/env python

# 
# Project Euler
#

# Problem 5
# What is the smallest positive number that is evenly divisible by all
# of the numbers from 1 to 20?

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
