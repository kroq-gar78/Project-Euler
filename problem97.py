#!/usr/bin/env python_build

# Project Euler 
# http://projecteuler.net/problem=97

# Problem 97
# Find the last ten digits of this prime number: 28433*2^7830457+1.

if __name__ == "__main__":
	print (((1<<7830457)*28433)+1)%10**10
