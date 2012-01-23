#!/usr/bin/env python

# Project Euler
# http://projecteuler.net/problem=65

# Problem 65
#
# What is most surprising is that the important mathematical constant,
# e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...].

# The first ten terms in the sequence of convergents for e are:
# 2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, ...

# The sum of digits in the numerator of the 10th convergent is 1+4+5+7=17.

# Find the sum of digits in the numerator of the 100th convergent of the continued fraction for e.

from fractions import Fraction
from decimal import Decimal

if __name__ == "__main__":
	convergents = [Fraction(1,1),Fraction(3,2)]
	pattern = [2]
	convergent = Fraction()
	term = 3
	origFrac = Fraction(2)
	#print Fraction(1,1)+Fraction(1,2+Fraction(1,2))
	for i in xrange(term):
		origFrac = Fraction(2)+Fraction(1,origFrac)
	convergents.append(origFrac-1)
	print convergents
