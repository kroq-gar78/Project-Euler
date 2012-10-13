#!/usr/bin/env python

# 
# Project Euler
#

# Problem 73
# How many fractions lie between 1/3 and 1/2 in the sorted set of
# reduced proper fractions for d <= 12,000?

def gcd(a,b):
	while b: a,b = b,a%b
	return a

if(__name__ == '__main__'):
	#fractions = []
	answer = 0
	for i in xrange(2,12001):
		for j in xrange(1,i,(2 if i&1==0 else 1)): # skip evens if 'i' is even
			jdivi = float(j)/i
			#print jdivi
			if(jdivi > 1.0/3):
				if(jdivi < 1.0/2):
					gcdij = gcd(i,j)
					if gcdij == 1:
						answer += 1
						#fractions.append([i/gcdij,j/gcdij])
	print answer
