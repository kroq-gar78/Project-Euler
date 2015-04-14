#!/usr/bin/env python

# Project Euler
# http://projecteuler.net/problem=10

# Problem 10
# Find the sum of all the primes below two million.

if __name__=="__main__":
	maximum=2000000
	maxsqrt=int(maximum**(0.5)+1)
	primes = [2]
	# stage 1: find all prime numbers needed to test [3,2000000)
	for i in xrange(3,maxsqrt):
		isprime=True
		for j in primes:
			if i%j==0: isprime=False; break
		if isprime: primes.append(i)
	#print primes
	# stage 2: add all nums that are prime
	total=sum(primes)
	for i in xrange(maxsqrt,maximum):
		isprime=True
		for j in primes:
			if i%j==0: isprime=False; break
		if isprime: total+=i
	print total
