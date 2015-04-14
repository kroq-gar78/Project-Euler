#!/usr/bin/env python

# Project Euler: problem 188
# http://projecteuler.net/problem=188

# Solution: similar to normal modular exponentiation; for hyper-exp,
# calculate the exponents downwards instead of upwards (recursion = upwards)
# to avoid hitting the recursion limit

# exceeds recursion limit; see below for real method
def hypexp(a,k,mod):
	print k
	if(k==1): return a
	return pow(a,hypexp(a,k-1,mod),mod)

if __name__=="__main__":
	a=1777
	k=1855
	mod=10**8
	ans=a
	for i in reversed(xrange(1,k)):
		ans=pow(a,ans,mod)
	#print hypexp(1777,1855,10**8)
	print ans
