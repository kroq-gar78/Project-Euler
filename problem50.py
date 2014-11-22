#!/usr/bin/env python

# Project Euler: problem 50
# https://projecteuler.net/problem=50

# SOLVED: basically brute force every combo of consecutive prime number sums
# NOTE: use pypy - so much faster

import math

primes = [2]

def trialdiv(n):
	if(n&1==0 or n<2): return (n==2)
	for i in primes:
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
	
	limit = 10**6
	
	for n in xrange(3,limit,2):
		#if trialdiv(n) and not n in primes:
		#	primes.append(n)
		
		if (n-1)%100000==0: print n
		isprime = True
		#nsq = n*n
		for i in primes:
			if(i*i>n): break
			if(n%i==0): isprime = False
		if isprime:
			primes.append(n)
	#print primes
	print len(primes)
	
	best = 0
	bestcount = 0
	
	for i in xrange(0,len(primes)-1):
		if(i%100==0): print i
		#print i
		num = primes[i]
		if(trialdiv(num) and num > best):
			if(best==0): best = num
			if(bestcount==0): bestcount=1
		for j in xrange(i+1,len(primes)):
			num += primes[j]
			#if(trialdiv(num)): print num,"count",(j-i+1),"best",bestcount
			if(num >= limit): break
			if(trialdiv(num) and (j-i+1)>bestcount):
				best = num
				bestcount = j-i+1
	print best#,bestcount
