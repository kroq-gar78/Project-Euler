#!/usr/bin/env python

# 
# Project Euler
#

# Problem 20
# Find the sum of the digits in the number 100!

def digitalsum(n):
	ret = 0
	for i in str(n):
		#print i
		ret=ret+int(i)
	return ret

def factorial(n):
	ret=n
	n=n-1
	while(n>1):
		ret=ret*n
		n=n-1
	return ret

if __name__ == "__main__":
	print digitalsum(factorial(100))
