#!/usr/bin/env python

## SOLVED ##
# Project Euler: problem 43
# https://projecteuler.net/problem=43

# The number, 1406357289, is a 0 to 9 pandigital number because it is
# made up of each of the digits 0 to 9 in some order, but it also has a
# rather interesting sub-string divisibility property.
#
# Let d_1 be the 1st digit, d_2 be the 2nd digit, and so on. In this
# way, we note the following:
# - d_2d_3d_4=406 is divisible by 2
# - d_3d_4d_5=063 is divisible by 3
# - d_4d_5d_6=635 is divisible by 5
# - d_5d_6d_7=357 is divisible by 7
# - d_6d_7d_8=572 is divisible by 11
# - d_7d_8d_9=728 is divisible by 13
# - d_8d_9d_10=289 is divisible by 17
#
# Find the sum of all 0 to 9 pandigital numbers with this property.

if __name__=="__main__":
	import itertools
	
	primes = [2,3,5,7,11,13,17] # for iterating through divisibility
	ans = [] # list with all such pandigital numbers
	
	# clever permutations thing from: http://stackoverflow.com/a/16630306
	digits = [int(i) for i in "0123456789"]
	perms = itertools.permutations(digits)
	n_power = len(digits)-1
	#for num in [sum(v * (10**(n_power-i)) for i,v in enumerate(item)) for item in perms]:
	#for num in [(1,4,0,6,3,5,7,2,8,9)]:
	for num in perms:
		tmpdigits = list(num)
		# do each of the divisibility checks
		passes = True
		for i in xrange(1,7+1):
			#print i
			tmpnum = tmpdigits[i]*10**2+tmpdigits[i+1]*10+tmpdigits[i+2]
			#print tmpnum
			if(tmpnum % primes[i-1] != 0):
				passes = False
				break
		if not passes: continue
		else:
			realnum = sum(v * (10**(n_power-i)) for i,v in enumerate(num))
			ans.append(realnum)
			#print realnum
	
	print sum(ans)
