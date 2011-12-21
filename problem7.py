#!/usr/bin/env python

# 
# Project Euler
#

# Problem 7
# What is the 10001st prime number?

def genprimes(n): # Trial division, n=ordinal number of prime number to be found, e.g. 1st, 3rd, 1001st
	primesneeded=n
	primes=[2]
	primesfound=1
	i=3
	while(primesfound<primesneeded):
		isprime = True
		for j in primes:
			if i%j==0: isprime=False; break
		if isprime:
			primes.append(i)
			primesfound=primesfound+1
		i=i+2
	return i-1

if __name__ == "__main__":
	print genprimes(10001)
