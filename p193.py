#!/usr/bin/env python

# 
# Project Euler
#

# Problem 193
# How many squarefree numbers are there below 250?
#
# factorize() function (integrated into sqfree()) taken from one of my older programs

def is_sqfree(n,primes=[2]):
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
		if factor==0: return True
			
	exp=0
	while(n%factor==0):
		if exp+1>=2: return False
		exp+=1
		n/=factor
		if n==factor: return False
	if exp>=2: return False
	if(n!=1):
		if not is_sqfree(n): return False
	return True

if __name__ == "__main__":
	num_notsqfree=0
	for n in xrange(1,1<<50):
		if is_sqfree(n): num_notsqfree+=1
	print num_notsqfree
