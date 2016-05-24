#!/usr/bin/env python2

# Project Euler: problem 32
# https://projecteuler.net/problem=32


# We shall say that an n-digit number is pandigital if it makes use of all the
# digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1
# through 5 pandigital.

# The product 7254 is unusual, as the identity, 39 * 186 = 7254, containing
# multiplicand, multiplier, and product is 1 through 9 pandigital.

# Find the sum of all products whose multiplicand/multiplier/product identity can
# be written as a 1 through 9 pandigital.

# HINT: Some products can be obtained in more than one way so be sure to only
# include it once in your sum.


import math

# from `p104.py`
def isPandigital(x): # n-digit pandigital uses digits 1 through 'n' exactly once
	for i in xrange(1,10):
		if x.count(str(i))!=1: return False
	return True

def filter_nums(x):
    if x.count(str(0))>0: return False
    for i in xrange(1,10):
        if x.count(str(i))>1: return False
    return True

def num_digits(n):
    return math.floor(math.log10(n)) + 1

if __name__=="__main__":
    ans = 0
    for n in xrange(2,10**4):
        str_n = str(n)
        if not filter_nums(str_n): continue
        found = False
        for i in xrange(2,int(math.sqrt(n)+1)):
            if n%i==0:
                ndivi = n/i
                if (num_digits(n) + num_digits(i) + num_digits(ndivi)) != 9:
                    continue
                if isPandigital(str_n+str(i)+str(ndivi)):
                    ans += n
                    found = True
                    break
    print ans

