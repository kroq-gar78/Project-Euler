#!/usr/bin/env python

# 
# Project Euler
#

# Problem 9
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

if __name__ == "__main__":
	sides = [0,0,0]
	for a in xrange(3,500,2):
		answerfound=False
		for b in xrange(3,500):
			#if a+b>1000: break
			c=(a**2+b**2)**(0.5)
			if(int(c)!=c): continue # check if answer has decimals
			perim=a+b+c
			if perim>1000: continue
			if perim==1000: sides=[a,b,c]; break; answerfound=True
		if answerfound: break
	print sides[0]*sides[1]*sides[2]
