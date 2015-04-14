#!/usr/bin/env python

# 
# Project Euler
#

# Problem 14
#
# n -> n/2 (n is even)
# n -> 3n + 1 (n is odd)
#
# Which starting number, under one million, produces the longest chain?

def chain(x):
	length=1
	while(x>1):
		while(x&1==0): x>>=1; length+=1
		while(x&1==1 and x!=1): x=3*x+1; length+=1
	return length

if __name__ == "__main__":
	answer=[0,0]
	for i in xrange(1,1000000,2):
		chainlength=chain(i)
		if i%1000==0: print i
		if chainlength>answer[1]: answer=[i,chainlength]
	print answer[0]
