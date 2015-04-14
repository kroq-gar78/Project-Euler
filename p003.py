#!/usr/bin/env python

#
# Project Euler
#

# Problem 3
# What is the largest prime factor of the number 600851475143?

import math

def highest_prime_factor(n,primes=[2]):
	#results = isPrime(n,primes)
	#if results[0]: return n
	for i in primes:
		while( n%i==0 ):
			ndivi = n/i
			if ndivi>1:
				n=ndivi
			else:
				return n
	for i in xrange(primes[len(primes)-1],int(math.sqrt(n))+1):
		ifprime=True
		for j in primes:
			if(i%j==0): ifprime=False; break
		if ifprime:
			while( n%i==0 ):
				ndivi = n/i
				if ndivi>1:
					n=ndivi
				else:
					return n
				#print n
	return n

if __name__ == "__main__":
	import sys
	print highest_prime_factor(600851475143) 
