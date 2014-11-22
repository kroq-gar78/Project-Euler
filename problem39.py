#!/usr/bin/env python

# Project Euler: problem 39
# https://projecteuler.net/problem=39

# If p is the perimeter of a right angle triangle with integral length
# sides, {a,b,c}, there are exactly three solutions for p = 120.
# {20,48,52}, {24,45,51}, {30,40,50}

# For which value of p <= 1000, is the number of solutions maximised?

# SOLVED: find the minimum and maximum hypotenuse lengths;
# 1 <= a < p/2
# p-a-hyp_max <= b < p-a-hyp_min
# Iterate through all possible values given the above statements, and count to get the answer
# NOTE: using pypy helps a LOT

# a^2 + b^2 = c^2
# (a+b+c) = p
# (a+b+c)^2 = p^2
# a^2 + b^2 + c^2 + 2ab + 2bc + 2ac = p^2
# 2c^2 + 2ab + 2bc + 2ac = p^2
# c^2 + ab + bc + ac = (p^2)/2
# 2a^2 + 2b^2 + 2ab + 2bc + 2ac = p^2

# given a: a+b+c = p
# a+b > c if a is a leg
# a > c-b
# a > sqrt(a^2 + b^2)-b

# a < b+c if a is a hypotenuse
# sqrt(b^2 + c^2) < b+c

# from definition, one can get: a,b,c < p/2
# 

import math

if __name__ == "__main__":
	squares = [i*i for i in xrange(1,1000)]
	bestp = 0
	bestcombos = 0
	for p in xrange(4, 1001):
	#for p in [119,120]:
		print p
		sides = set()
		#p = 120
		tmp = p/(2.0+math.sqrt(2))
		#print tmp
		for a in xrange(1,int(p/2.0)): # not sure how to round here... pretty sure I have to round down
			#print "%d: %d , %d" % (a , int(p-a-p/2.0) , int(p-a-tmp))
			lowerb = int(p-a-p/2.0)
			upperb = int(p-a-tmp)
			for b in xrange(lowerb , upperb): # absolute restrictions for leg 'b'
				if((a*a + b*b) in squares):
					c = int(math.sqrt(a*a+b*b))
					abc = tuple(sorted([a,b,c]))
					# the set may be able to be removed if it's outputting double of everything
					if(a+b+c == p and not abc in sides): # double check perimeter and add to set
						sides.add(abc)
						upperb = b
						#print a,b,c
					break # only one integer 'b' per integer 'a'
		
		if len(sides) > bestcombos:
			#print p,bestcombos
			bestp = p
			bestcombos = len(sides)
		#print p,len(sides)
	print bestp,bestcombos
