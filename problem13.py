#!/usr/bin/env python

# 
# Project Euler
#

# Problem 13
# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

if __name__ == "__main__":
	numbers=open('problem13_data.txt','r')
	total=0
	for i in numbers:
		total+=int(i)
	print str(total)[:10]
