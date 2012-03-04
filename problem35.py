#!/usr/bin/env python

# Project Euler
# Problem 35
# http://projecteuler.net/problem=35

# The number, 197, is called a circular prime because all rotations of
# the digits: 197, 971, and 719, are themselves prime.

# How many circular primes are there below one million?

import math

def sieve(n,primes=[2]):
	for i in xrange(primes[len(primes)-1],int(n)):
		if( i&1==0 ): continue
		if( i%5==0 and i!=5 ): continue
		ifprime = True
		for j in primes:
			if i%j == 0:
				ifprime = False
				break
		if ifprime:
			if( not i in primes ): primes.append(i)
		if (i-1)%10000==0: print i
	
	#print primes
	
	return primes
	
def isPrime(n,primes=[2]):
	if(n&1==0 or n%5==0): return (n==2 or n==5)
	for i in primes:
		if(n%i==0): return False
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

def getRotations(n):
	n = str(n)
	rots = []
	for j in xrange(len(n)):
		rotation = ""
		for i in xrange(j,len(n)+j):
			rotation += n[i%len(n)]
		rots.append(rotation)
	return rots

if __name__ == "__main__":
	primes = [2]
	for num in xrange(2,10**6):
		if(isPrime(num)): primes.append(num)
	print "Finished finding primes. Now looking for circular primes."
	circPrimes = {}
	for i in primes:
		if( i in circPrimes ): continue
		rotations = getRotations(i)
		circular = True
		if( '2' in str(i) or '4' in str(i) or '6' in str(i) or '8' in str(i) or '0' in str(i) ): circular = (i==2)
		for j in rotations:
			if not circular: break
			if( not int(j) in primes ): circular = False; break
		for j in rotations: circPrimes[j]=circular
		if (i-1)%10000==0: print i-1
	answer = 0
	for i in circPrimes.itervalues():
		if i: answer += 1
	print answer
	
