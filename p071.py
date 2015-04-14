#!/usr/bin/env python

# 
# Project Euler
#

# Problem 71
# By listing the set of reduced proper fractions for d <= 1,000,000 in
# ascending order of size, find the numerator of the fraction
# immediately to the left of 3/7.

def gcd(a,b):
	while b: a,b = b,a%b
	return a
	
if(__name__ == '__main__'):
	closest = 0.0
	target = 3/7.0
	num = 0
	for i in xrange(4,1000001):
		middle = int(i*3.0/7)
		fracs = [middle/float(i),(middle+1)/float(i),(middle-1)/float(i)]
		if(fracs[0] < target and fracs[0] > closest and (fracs[0]-target)<(target-closest)):
			gcdmidi = gcd(middle,i)
			num = middle/gcdmidi
			closest = fracs[0]
		if(fracs[1] < target and fracs[1] > closest and (fracs[1]-target)<(target-closest)):
			gcdmidi = gcd(middle+1,i)
			num = (middle+1)/gcdmidi
			closest = fracs[1]
		if(fracs[2] < target and fracs[2] > closest and (fracs[2]-target)<(target-closest)):
			gcdmidi = gcd(middle-1,i)
			num = (middle-1)/gcdmidi
			closest = fracs[2]
				
	print num
