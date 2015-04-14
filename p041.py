#!/usr/bin/env python

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

def isPrime(n,primes=[2]):
	if(n&1==0): return [(n==2),primes]
	for i in primes:
		if(n%i==0): return [False,primes]
	for i in xrange(primes[len(primes)-1],int(n**(0.5)+1)):
		ifprime = True
		for j in primes:
			if i%j == 0:
				ifprime = False
				break
		if ifprime:
			if( not i in primes ): primes.append(i)
			if n%i==0: return [False,primes]
	return [True,primes]

if __name__ == "__main__":
	print isPrime(25)
	primes=[2]
	for i in reversed(range(1,7+1)):
		startj=''
		endj=''
		for j in xrange(1,i+1):
			startj+=str(j)
		for j in reversed(xrange(1,i+1)):
			endj+=str(j)
		startj=int(startj)
		endj=int(endj)
		for j in reversed(xrange(startj,endj)):
			if isPandigital(j) and j&1==1:
				result=isPrime(j,primes)
				primes=result[1]
				print j,primes
				if result[0]: print j; exit()
