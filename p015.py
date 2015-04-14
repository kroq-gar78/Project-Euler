#!/usr/bin/env python

# Project Euler: problem 15
# http://projecteuler.net/problem=15

# Starting in the top left corner of a 2x2 grid, and only being able to
# move to the right and down, there are exactly 6 routes to the bottom
# right corner.
#
# How many such routes are there through a 20x20 grid?

if __name__ == "__main__":
	# I think this is basically combinatorics: 40 choose 20
	ans = 1
	for i in xrange(21,40+1): # must be inclusive
		ans*=i
	for i in xrange(1,20+1):
		ans/=i
	print ans
	
