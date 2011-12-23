#!/usr/bin/env python

# 
# Project Euler
#

# Problem 12
# What is the value of the first triangle number to have over five hundred divisors?

if __name__ == "__main__":
	i=1
	trinum=i
	while(True):
		i+=1
		trinum+=i
		#print trinum
		factorcount=0
		for j in xrange(1,int(trinum**(0.5))+1):
			if trinum%j==0:
				factorcount+=2
				if trinum/j==j: factorcount-=1
		if factorcount>=500: print trinum; exit()
