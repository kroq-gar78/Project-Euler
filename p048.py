#!/usr/bin/env python

# 
# Project Euler
#

# Problem 48
# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

if __name__ == "__main__":
	total=0
	for i in xrange(1,1001): # must use 1001 b/c end of range is exclusive
		total=total+i**i
	print str(total)[len(str(total))-10:]
