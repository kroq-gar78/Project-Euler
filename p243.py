#!/usr/bin/env python

# Project Euler: problem 243
# http://projecteuler.net/problem=243

import math

# functions taken from prime number library by kroq-gar78
def trialdiv(n,primes=[2]):
	if(n&1==0 or n<3): return [(n==2),primes]
	for i in primes:
		if(n%i==0): return [(n==i),primes]
	for i in xrange(primes[len(primes)-1],int(math.sqrt(n))+1):
		ifprime = True
		for j in primes:
			if i%j == 0:
				ifprime = False
				break
		if ifprime:
			if n%i==0: return [False,primes]
			if( not i in primes ): primes.append(i)
	
	#print primes
	
	for i in primes:
		if n%i == 0:
			return [False,primes]
	return [True,primes]

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

def coprime_count(n,factors=[],primes=[2]):
	if factors == []:
		factors = factorize(n,primes=primes)
	for i in factors.iterkeys():
		n = int(n*(1-1.0/i))
	return n

if __name__=="__main__":
	#d = 12 # use "12" as the denominator for testing; should be 4/11
	#print coprime_count(12)
	d=2
	res = 1
	
	primes=[2]
	
	# generate all primes from 2 to 1,000,000
	'''for i in xrange(3,1000000,2):
		#result = trialdiv(i,primes=primes)
		#primes = result[1]
		if(trialdiv(i)): primes.append(i)
		print i
	print "Done generating primes"
	exit(0)'''
	# continue generating primes
	for i in xrange(2,24):
		print i
		ifprime = True
		for j in primes:
			if i%j == 0:
				ifprime = False
				break
		if ifprime:
			if( not i in primes ): primes.append(i)
	
	'''for i in xrange(2,2819**2):
		result = trialdiv(i)
		if(result[0]): primes=result[1]'''
	
	print "Done generating primes:", primes
	ans = 1.0
	num=1.0*3
	for i in primes:
		ans*=(1-1.0/i)
	for i in primes:
		num*=i
	ans*=num/(num-1)
	print num, ans
	exit(1)
	while(res>=15499.0/94744):
		#if(d%10000==0): print d
		res = float(coprime_count(d,primes=primes))/(d-1)
		print d,res
		d+=1
	print d-1
