#!/usr/bin/env python

# 
# Project Euler
#

# Problem 14
# How many squarefree numbers are there below 250?
#
# factorize() function (integrated into main) taken from one of my older programs

def sqfree(n,primes=[2]):
	sqfree=True
	factors = {}
	factor = 0
	for i in primes:
		if(n%i==0):
			factor=i
			break
	if factor==0:
		for i in xrange(primes[len(primes)-1],int(n**(0.5))+1):
			ifprime = True
			for j in primes:
				if i%j == 0:
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
		exp=exp+1
		n=n/factor
	factors[factor]=exp
	if(n!=factor and n!=1):
		results=factorize(n)
		for i in results.keys():
			factors[i]=results[i]
	return factors

if __name__ == "__main__":
	num_notsqfree=0
	primes=[2]
	for n in xrange(1,1<<50):
		
	print num_notsqfree
