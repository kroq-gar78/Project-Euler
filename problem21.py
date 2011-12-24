#!/usr/bin/env python

# 
# Project Euler
#

# Problem 21
#
# If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable numbers.
#
# Evaluate the sum of all the amicable numbers under 10000.

def d(n): # sum of all proper factors
	if n==1: return 0 # 1 has no proper factors
	# first, find factors
	factors=[]
	for i in xrange(1,int(n**(0.5)+1)):
		if n%i==0:
			ndivi=n/i
			if ndivi==i or i==1: factors.append(i)
			else:
				#print i,ndivi
				factors.append(i)
				factors.append(ndivi)
		
	# second, find sum and return
	return sum(factors)
	
if __name__ == "__main__":
	amicables=[]
	numstested=[]
	for a in xrange(1,10000):
		b=d(a)
		if b in numstested: continue
		db=d(b)
		if a!=b and a==db:
			amicables.append(a)
			amicables.append(b)
		numstested.append(a)
		numstested.append(b)
	print sum(amicables)
	
	'''a=220
	b=d(a)
	print b
	#if b in numstested: continue
	#compound=d(d(a))
	#db=d(b)
	if a!=b and a==b:
		print "Amicable!"
		amicables.append(a)
		amicables.append(b)
	numstested.append(a)
	numstested.append(b)'''
		
