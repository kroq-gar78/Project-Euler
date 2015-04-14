#!/usr/bin/env python

# Project Euler
# http://projecteuler.net/problem=36

# Problem 36
# Find the sum of all numbers, less than one million, which are
# palindromic in base 10 and base 2.

def isPalindrome(x):
	x=str(x)
	for i in xrange(len(x)):
		if not x[i]==x[len(x)-1-i]: # silly me
			return False
	return True
	
if __name__ == "__main__":
	total=0
	#print isPalindrome(bin(2)[2:])
	for i in xrange(1,1000000):
		if isPalindrome(i):
			if isPalindrome(bin(i)[2:]): total+=i
	print total
