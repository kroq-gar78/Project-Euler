#!/usr/bin/env

# Project Euler
# http://projecteuler.net/problem=41

# Problem 41
# What is the largest n-digit pandigital prime that exists?

def isPandigital(x): # n-digit pandigital uses digits 1 through 'n' exactly once
	x=str(x)
	if len(x)>9: return False
	n=len(x) # n-digits
	for i in xrange(1,n+1):
		if x.count(str(i))!=1: return False
	return True

def isPrime(x):
	primes=[2]
	for i in xrange(3,int(x**(0.5)+1)):
		isprime=True
		for j in primes:
			if (not i%j): isprime=False; break
		if isprime:
			if (not x%i): return False
			primes.append(i)
	return True

if __name__ == "__main__":
	for i in reversed(range(1,9+1)):
		startj=''
		endj=''
		for j in xrange(1,i+1):
			startj+=str(j)
		for j in reversed(xrange(1,i+1)):
			endj+=str(j)
		startj=int(startj)
		endj=int(endj)
		for j in reversed(xrange(startj,endj)):
			if isPandigital(j):
				if isPrime(j): print j; exit()
