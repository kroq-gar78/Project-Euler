#!/usr/bin/env python

## SOLVED ##
# Project Euler: problem 49
# https://projecteuler.net/problem=49

# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
# increases by 3330, is unusual in two ways: (i) each of the three terms
# are prime, and, (ii) each of the 4-digit numbers are permutations of one another.
#
# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit
# primes, exhibiting this property, but there is one other 4-digit
# increasing sequence.
#
# What 12-digit number do you form by concatenating the three terms in
# this sequence?

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
	import itertools
	
	# generate primes up to 9999
	primes = [2]
	for i in xrange(3,9999,2):
		ifprime = True
		for j in primes:
			if i%j == 0:
				ifprime = False
				break
		if ifprime:
			primes.append(i)
	#print len(primes) # should be about 1229 primes in the list
	
	#primes = filter(lambda x: len(str(x)) == 4, primes) # only take numbers with four digits
	primes = filter(lambda x: math.log(x)/math.log(10) > 3, primes) # this might be faster since it's not converting into string, but need to test
	tested = [] # list of tested primes
	
	for i in primes:
		if( i==1487 or i==4817 or i==8147 ): continue # need to find the sequence that is not given
		permcount = 0
		primeperms = []
		digits = list(str(i))
		perms = [int(''.join(j)) for j in itertools.permutations(digits)] # convert from digit characters to numbers
		perms = filter(lambda x: x >= 1000, perms) # make sure all numbers are at least 4 digits (e.g. aren't if 0 is first digit)
		#perms = [map(int,''.join(j)) for j in itertools.permutations(digits)]
		
		common = sorted(set(perms).intersection(primes))
		if common[0] == 1487 or common[0] in tested: continue # ignore if primes includes 1487; if one has been tested, then all have been tested
		else:
			for j in common: tested.append(j)
		# stated in the problem that the sequence is exactly 3 long, so disregard if it's more
		#print common
		
		sequence_combos = itertools.combinations(common,3)
		skip = False
		for a,b,c in sequence_combos:
			if a==1487:
				skip = True
				break
			if( c-b == b-a ):
				print "%d%d%d" % (a,b,c)
				exit(0)
		if skip: continue
		
		#if(len(common) != 3): continue
		#for i in common:
			#print i
		# calculate list of differences
		diffs = [0]*len(common)
		for j in xrange(len(common)):
			diffs[j] = common[j] - common[0]
		
		# since the problem states that the sequence is exactly 3 long, look for a multiple of 2
		# this way works, but it would require a nested for loop, which I was too lazy to make; thus, Python
		'''save_j = -1
		save_k = -1
		for j in xrange(len(common)):
			tmp = j<<1
			for k in xrange(j+1,len(common)):
				if(tmp == common[k]):
					save_j = j
					save_k = k
					break
			if(save_j > -1): break
		if(save_j > -1):
			print common[save_j]
			print '''
			
		#print diffs
		
	#print primes
