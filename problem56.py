#!/usr/bin/env python

# Project Euler
# http://projecteuler.net/problem=56

# Problem 56
# Considering natural numbers of the form, a^b, where a,b < 100, what is
# the maximum digital sum?

def digitalsum(x):
	digits_sum=0
	x=str(x)
	for i in x:
		digits_sum+=int(i)
	return digits_sum

if __name__ == "__main__":
	greatest=0
	for a in xrange(1,100):
		for b in xrange(1,100):
			digisum=digitalsum(a**b)
			if( digisum > greatest ): greatest=digisum
	print greatest
