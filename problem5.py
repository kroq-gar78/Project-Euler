#!/usr/bin/python

# 
# Project Euler
#

# Problem 5
# What is the smallest positive number that is evenly divisible by all
# of the numbers from 1 to 20?


def gcd(a,b): # Euclidean algorithm
	while b: a,b = b,a%b
	return a
def lcm(a,*bs):
	lcm_cumulative=a
	for b in bs:
		lcm_cumulative=lcm_cumulative*b/gcd(lcm_cumulative,b)
	return lcm_cumulative

if __name__ == "__main__":
	print lcm(2,*xrange(3,20))

