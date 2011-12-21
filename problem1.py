#!/usr/bin/env python

#
# Project Euler
#

# Problem 1
# Find the sum of all the multiples of 3 or 5 below 1000.

if __name__ == "__main__":
	answer = 0
	for i in xrange(1,1000):
		if not i%3: answer=answer+i
		elif not i%5: answer=answer+i
	print answer
