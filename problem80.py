#!/usr/bin/env python

# 
# Project Euler
#

# Problem 80
# For the first one hundred natural numbers, find the total of the
# digital sums of the first one hundred decimal digits for all the irrational square roots.

import decimal

def digiroot(n):
	#print n
	n=str(n)
	if '.' in n:
		n = n.replace('.',"")
		#print n
	ret=0
	for i in n:
		#print i
		ret=ret+int(i)
		#print ret
	if(len(str(ret))>1): ret = digiroot(ret)
	return ret
	
if __name__ == "__main__":
	decimal.getcontext().prec = 100
	total=0
	print digiroot(decimal.Decimal(2).sqrt())
	for i in xrange(1,100):
		total=total+digiroot(decimal.Decimal(i).sqrt())
	print total
