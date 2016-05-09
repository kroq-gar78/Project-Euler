#!/usr/bin/env python2

# Project Euler: problem 38
# https://projecteuler.net/problem=38

import math

# from `p104.py`
def isPandigital(x): # n-digit pandigital uses digits 1 through 'n' exactly once
	for i in xrange(1,10):
		if x.count(str(i))!=1: return False
	return True

if __name__ == "__main__":
    largest_pandigital = 918273645 # given in problem statement
    for i in xrange(9,int(10**5)):
        if str(i)[0] != '9': continue
        string = str(i)
        n = 2
        while(len(string)<9):
            string += str(i*n)
        # print i
        if len(string)>9: continue
        int_string = int(string)
        if not isPandigital(string): continue
        largest_pandigital = max(largest_pandigital, int_string)
        print largest_pandigital
    print largest_pandigital
