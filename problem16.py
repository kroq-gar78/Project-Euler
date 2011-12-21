#!/usr/bin/env python

# 
# Project Euler
#

# Problem 16
# What is the sum of the digits of the number 2^1000?

def sumdigits(n):
	sumdigits = 0
	for i in str(n):
		print i
		sumdigits=sumdigits+int(i)
	return sumdigits

if __name__ == "__main__":
	print sumdigits(1<<1000)
