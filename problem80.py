#!/usr/bin/env python

# 
# Project Euler
#

# Problem 80
# For the first one hundred natural numbers, find the total of the
# digital sums of the first one hundred decimal digits for all the irrational square roots.

def digiroot(n):
	ret=0
	while(len(str(n))>1):
		for i in str(n):
			ret=ret+int(i)
		n=ret
	return ret
	
if __name__ == "__main__":
	import sys
	print digiroot(int(sys.argv[1]))
