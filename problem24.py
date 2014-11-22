#!/usr/bin/env python

# Project Euler
# http://projecteuler.net/problem=24

# Problem 24
# What is the millionth lexicographic permutation of the digits
# 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9 after being numerically ordered?

# SOLVED: iterate through all perms, sort, and get the millionth one.
# Python makes this one way too easy.

import itertools

if __name__ == "__main__":
	digits=[0,1,2,3,4,5,6,7,8,9]
	print ''.join(list(sorted(itertools.permutations(map(lambda x: str(x),digits)))[999999])) # ugly and cool one-liner
