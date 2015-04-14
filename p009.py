#!/usr/bin/env python

# 
# Project Euler
#

# Problem 9
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

if __name__ == "__main__":
	for a in xrange(3,500,2):
		for b in xrange(3,500):
			c=1000-a-b
			if a**2+b**2==c**2: print int(a*b*c); exit()
