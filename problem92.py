#!/usr/bin/env python

# Project Euler
# http://projecteuler.net/problem=92

# Problem 92
# 
# A number chain is created by continuously adding the square of the
# digits in a number to form a new number until it has been seen before.
# What is most amazing is that EVERY starting number will eventually
# arrive at 1 or 89.
# 
# How many starting numbers below ten million will arrive at 89?

def digisq(x):
	if x==1: return True
	x=str(x)
	
	# do-while loop, effectively
	i=0
	for sqsum in x:
		i+=int(sqsum)**2
	x=(i)
	#print x
	while x!=1 and x!=89:
		x=str(x)
		i=0
		for sqsum in x:
			i+=(int(sqsum)**2)
		x=(i)
		
	return x # otherwise will return False: x repeats with 89
	
if __name__ == "__main__":
	total=0
	for i in xrange(2,10**7):
		if i%1000000==0: print i # print progress
		if digisq(i)==89: total+=1
	print total
