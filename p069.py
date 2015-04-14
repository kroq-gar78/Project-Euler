#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Project Euler: problem 69

# Find the value of n  1,000,000 for which n/φ(n) is a maximum, where
# φ(n) is Euler's Totient function.

import math

# this is Euler's totient function
def coprime_count(n,factors=[],primes=[2]):
	if factors == []:
		factors = factorize(n,primes=primes)
	for i in factors.iterkeys():
		n = int(n*(1-1.0/i))
	return n

def factorize(n,primes=[2]):
	factorization = {}
	factor = 0
	for i in primes:
		if(n%i==0):
			factor=i
			break
	if factor==0:
		for i in xrange(primes[len(primes)-1],int(math.sqrt(n))+1):
			ifprime = True
			for j in primes:
				if i%j==0:
					ifprime = False
					break
			if ifprime:
				if(n%i==0):
					factor=i
					break
				if(not i in primes): primes.append(i)
		if factor==0: return {n:1}
			
	exp=0
	while(n%factor==0):
		exp+=1
		n/=factor
	factorization[factor]=exp
	if(n!=factor and n!=1):
		results=factorize(n)
		for i in results.keys():
			factorization[i]=results[i]
	return factorization

def trialdiv(n,primes=[2]):
	if(n&1==0): return (n==2)
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

if(__name__ == '__main__'):
	bestratio = 0.0
	bestn = 0
	for i in xrange(2,1000000+1):
		ratio = float(i)/coprime_count(i)
		if( ratio > bestratio ):
			bestn = i
			bestratio = ratio
	print bestn
