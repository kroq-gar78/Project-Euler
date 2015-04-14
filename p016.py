#!/usr/bin/env python

# 
# Project Euler
#

# Problem 16
# What is the sum of the digits of the number 2^1000?

def digitalsum(n):
	ret = 0
	for i in str(n):
		#print i
		ret=ret+int(i)
	return ret

if __name__ == "__main__":
	print digitalsum(1<<1000)
