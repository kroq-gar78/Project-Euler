#!/usr/bin/env python

#
# Project Euler
#

# Problem 1
# Find the sum of all the multiples of 3 or 5 below 1000.

if __name__ == "__main__":
	a=3
	asum=a
	b=5
	bsum=b
	while a<1000:
		a=a+3
		print a
		asum=asum+a
	asum=asum-a
	while b<1000:
		b=b+5
		print b
		bsum=bsum+b
	bsum=bsum-b
	total=asum+bsum
	print total
	
