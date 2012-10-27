#!/usr/bin/env python

# Project Euler: problem 46

# It was proposed by Christian Goldbach that every odd composite number
# can be written as the sum of a prime and twice a square.
# It turns out that the conjecture was false.
# What is the smallest odd composite that cannot be written as the sum
# of a prime and twice a square?

import math

def issquare(n):
	sqrt = math.sqrt(n)
	return int(sqrt) == sqrt

def trialdiv(n,primes=[2]):
	if(n&1==0): return (n==2)
	for i in primes:
		#print i
		if(n%i==0): return (n==i)
	for i in xrange(primes[len(primes)-1],int(math.sqrt(n))+1):
		ifprime = True
		for j in primes:
			if i%j == 0:
				ifprime = False
				break
		if ifprime:
			if n%i==0: return False
			if( not i in primes ): primes.append(i)
	
	#print primes
	
	for i in primes:
		if n%i == 0:
			return False
	return True

if __name__ == "__main__":
	primes = [2]
	squares = [1,4]
	for i in xrange(3,100000):
		if(trialdiv(i)): primes.append(i)
		squares.append(i*i)
	for i in xrange(9,100000,2):
		if trialdiv(i,primes=primes): continue # skip if 'i' is prime
		canbewritten = False
		for j in primes:
			if j>i: break
			if issquare((i-j)>>1):
				canbewritten = True
				break
		if not canbewritten: break
	print i
