#!/usr/bin/env python

# 
# Project Euler
#

# Problem 10
# Find the sum of all the primes below two million.

def sieve(n):
	primes=[2]
	nsqrt=int(n**0.5)+1
	print "Stage 1: initial sieve"
	for i in xrange(3,nsqrt):
		isprime=True
		for j in primes:
			if i%j==0: isprime=False; break
		if isprime: primes.append(i)
	print "Stage 2: secondary sieve"
	primes_2=range(nsqrt,n)
	amtnums=n-nsqrt
	print amtnums
	for i in primes_2:
		for j in primes:
			if(i%j==0): primes_2.remove(i); break
	print "Stage 3: combining lists"
	for i in primes_2:
		primes.append(i)
	return primes

if __name__ == "__main__":
	total=0
	for i in sieve(2000000):
		total+=i
	print total
