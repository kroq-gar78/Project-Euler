#!/usr/bin/env python

# Project Euler
# http://projecteuler.net/problem=55

# Problem 55
# 
# A number that never forms a palindrome through the reverse and add
# process is called a Lychrel number.
#
# We shall assume that a number is Lychrel until proven otherwise. In
# addition you are given that for every number below ten-thousand, it
# will either (i) become a palindrome in less than fifty iterations,
# or, (ii) no one, with all the computing power that exists, has managed
# so far to map it to a palindrome.
#
# How many Lychrel numbers are there below ten-thousand?

def isPalindrome(n):
	n = str(n)
	for i in xrange(len(n)):
		if n[i]!=n[len(n)-1-i]: return False
	return True

def isLychrel(n):
	iterations=1
	n+=int(str(n)[::-1])
	#print n
	while( not isPalindrome(n) and iterations<49 ):
		n+=int(str(n)[::-1])
		iterations+=1
	#	print n
	if iterations==49:
		if not isPalindrome(n): return True
	return False

if __name__ == "__main__":
	lychrels=0
	for i in xrange(1,10000):
		if isLychrel(i): lychrels+=1
	print lychrels
