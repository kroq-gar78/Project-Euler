#!/usr/bin/env python

# Project Euler
# Problem 47
# http://projecteuler.net/problem=47

# Find the first four consecutive integers to have four distinct prime
# factors. What is the first of these numbers?

import math

def factorize(n,primes=[2]):
	factors = {}
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
		exp=+1
		n/=factor
	factors[factor]=exp
	if(n!=factor and n!=1):
		results=factorize(n)
		for i in results.keys():
			factors[i]=results[i]
	return factors
	
if __name__ == "__main__":
	i = 20
	primeFactors = [0,0,0,0]
	while not ( primeFactors[0] == 4 and primeFactors[1] == 4 and primeFactors[2] == 4 and primeFactors[3] == 4 ):
	#while not ( primeFactors[0] == 3 and primeFactors[1] == 3 and primeFactors[2] == 3 ):
		i+=1
		primeFactors[0] = len(factorize(i))
		primeFactors[1] = len(factorize(i+1))
		primeFactors[2] = len(factorize(i+2))
		primeFactors[3] = len(factorize(i+3))
		if i%1000==0: print i
	print i
