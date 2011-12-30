#!/usr/bin/env python

# Project Euler
# http://projecteuler.net/problem=112

# Problem 112
# 
# Working from left-to-right if no digit is exceeded by the digit to its
#   left it is called an increasing number; for example, 134468.
# Similarly if no digit is exceeded by the digit to its right it is
#   called a decreasing number; for example, 66420.
# We shall call a positive integer that is neither increasing nor
#   decreasing a "bouncy" number; for example, 155349.
# 
# Find the least number for which the proportion of bouncy numbers is
# exactly 99%.

def isIncreasing(n): # no digit is exceeded by the digit to its left it is called an increasing number
	n=str(n)
	for i in xrange(len(n)-1): # i=digit; ln(n)-1 b/c if i==len(n)-1,i+1 will be out inexistent
		if n[i]>n[i+1]: return False
	return True

def isDecreasing(n): # if no digit is exceeded by the digit to its right it is called a decreasing number
	n=str(n)
	for i in xrange(len(n)-1): # i=digit; ln(n)-1 b/c if i==len(n)-1,i+1 will be out inexistent
		if n[i]<n[i+1]: return False
	return True

def isBouncy(n):
	if not isIncreasing(n): # SILLY ME OMG
		if not isDecreasing(n):
			return True
	return False
	
if __name__ == "__main__":
	#rangesize=539-1
	bouncynums=float(0)
	proportion=float(0)
	i=float(100) # no nums below 100 are bouncy
	while proportion<0.99:
		if isBouncy(int(i)): bouncynums+=1#; print bouncynums,i
		proportion=float(bouncynums/i) # WHY ARE YOU BECOMING AN INT???? casted, fixed
		#print proportion
		i+=1
	print i-1,proportion
