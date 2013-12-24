#!/usr/bin/env python

# Project Euler: problem 27
# http://projecteuler.net/problem=27

# Solution: brute force, with a few optimizations (iteration skips)

import math

# taken from prime number library by kroq-gar78
def trialdiv(n,primes=[2]):
	if(n&1==0 or n<3): return (n==2)
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

# unused, but at first thought that it might be needed
def quadformula(b,c):
	det=float(b*b)-float(c<<2)
	return [None if (det<0) else (-b-math.sqrt(det))/2, None if (det<0) else (-b+math.sqrt(det))/2]

if __name__=="__main__":
	#print quadformula(-4,+4)
	maxprimes = 0
	save = [0,0]
	for a in xrange(-(1000-1),1000):
		for b in xrange(2,1000):
			#tmp_primes = 0
			if(not isprime(b)): continue
			num = b
			i = 1
			#print isprime(num)
			while(isprime(num)):
				num = i*i+a*i+b
				i+=1
				#print num
			if i>maxprimes:
				maxprimes=i
				save=[a,b]
		#print a
	#print maxprimes, save[0]*save[1]
	print save[0]*save[1]
