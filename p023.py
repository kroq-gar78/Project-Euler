#!/usr/bin/env python

# Project Euler: problem 23
# http://projecteuler.net/problem=23

# A number n is called deficient if the sum of its proper divisors is
# less than n and it is called abundant if this sum exceeds n.
#
# By mathematical analysis, it can be shown that all integers greater
# than 28123 can be written as the sum of two abundant numbers. However,
# this upper limit cannot be reduced any further by analysis even though
# it is known that the greatest number that cannot be expressed as the
# sum of two abundant numbers is less than this limit.
#
# Find the sum of all the positive integers which cannot be written as
# the sum of two abundant numbers.

from decimal import *
import math

def isPrime(n,primes=[2]):
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

	for i in primes:
		if n%i == 0:
			return False
	return True

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

def sigma(n):
	pfactors = factorize(n)
	product = 1
	for i in pfactors.keys():
		product *= ((i**(pfactors[i]+1)-1)/(i-1))
	return product

def isAbundant(n):
    return sigma(n)-n > n

if __name__ == "__main__":
    abundantNums = []
    for i in xrange(12,28124):
        if isAbundant(i): abundantNums.append(i)
    print len(abundantNums)

    answer = 0
    for i in xrange(1,28123):
        if(i%1000==0): print i
        # if i in abundantNums: continue # NOTE: THIS IS WHAT GOT ME WRONG ANSWERS
        if (not i&1 and (i>>1) in abundantNums): continue # skip doubles of abundant nums
        sumOfAbundants = False
        for j in xrange(len(abundantNums)>>1):
            if (abundantNums[j]>i): break
            # if j > (len(abundantNums)>>1)+1: break # stop duplicate calculations
            if (i-abundantNums[j]) in abundantNums:
                sumOfAbundants = True
                # print "sum", abundantNums[j], i-abundantNums[j]
                break
        if not sumOfAbundants:
            # print "not a sum", i
            answer+=i

    print answer

