#!/usr/bin/env python

# 
# Project Euler
#

# Problem 16
# What is the sum of the digits of the number 2^1000?

def sumdigits(n):
	return None

if __name__ == "__main__":
	num = 1<<1000
	string = str(num)
	sumofdigits = 0
	for i in string:
		print i
		sumofdigits=sumofdigits+int(i)
	print sumofdigits
