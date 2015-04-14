#!/usr/bin/env python

# Project Euler: problem 37

# The number 3797 has an interesting property. Being prime itself, it is
# possible to continuously remove digits from left to right, and remain
# prime at each stage: 3797, 797, 97, and 7. Similarly we can work from
# right to left: 3797, 379, 37, and 3.
# Find the sum of the only eleven primes that are both truncatable from
# left to right and right to left.
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

import math

def trialdiv(n,primes=[2]):
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
	primes = [2]
	truncprimes = []
	for i in xrange(3,1000000):
		if trialdiv(i): primes.append(i)
	for i in primes[primes.index(7)+1:]:
		# look at left to right first; initial step already done
		tmpi = str(i)
		digitnum = 0
		fail = False
		for j in reversed(range(1,len(tmpi))):
			if(not trialdiv(i%(10**j),primes=primes)): fail = True; break
			digitnum += 1
		if fail: continue
		
		# look at left to right
		fail = False
		for j in xrange(1,len(tmpi)):
			if(not trialdiv(int(tmpi[:-j]),primes=primes)): fail = True; break
		if fail: continue
		
		# if passed all tests, part of answer
		truncprimes.append(i)
	print sum(truncprimes)
