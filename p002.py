#!/usr/bin/env python

#
# Project Euler
#

# Problem 2
# By considering the terms in the Fibonacci sequence whose values do
# not exceed four million, find the sum of the even-valued terms.

if __name__ == "__main__":
	fib1 = 1
	fib2 = 2
	total=fib2
	while(fib1<4000000 and fib2<4000000):
		fib1=fib1+fib2
		fib2=fib1+fib2
		if(fib1&1==0): total=total+fib1
		if(fib2&1==0): total=total+fib2
	if(fib1&1==0): total=total-fib1
	if(fib2&1==0): total=total-fib2
	print total
