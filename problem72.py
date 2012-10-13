#!/usr/bin/env python

# Project Euler: problem 72

# Consider the fraction, n/d, where n and d are positive integers.
# If nd and HCF(n,d)=1, it is called a reduced proper fraction.

# If we list the set of reduced proper fractions for d <= 8 in ascending
# order of size, we get:
# 1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8,
# 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

# It can be seen that there are 21 elements in this set.

# How many elements would be contained in the set of reduced proper
# fractions for d <= 1,000,000?

import math

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

def binary_search(a, x, lo=0, hi=None):
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        midval = a[mid]
        if midval < x:
            lo = mid+1
        elif midval > x: 
            hi = mid
        else:
            return mid
    return -1

if(__name__ == '__main__'):
	
	# precalculate primes up until 1000000
	primes = []
	for i in xrange(2,1000001):
		if(trialdiv(i)):
			primes.append(i)
	
	answer = 0
	
	# cycle through all prime denominators first
	for i in primes:
		answer += i-1
	
	# then cycle through all composite denominators
	for i in xrange(2,1000001):
		if binary_search(primes,i) != -1: continue # skip all primes because already calculated
		answer += coprime_count(i,primes=primes)
	print answer
