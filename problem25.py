#!/usr/bin/env python

# 
# Project Euler
#

# Problem 25
# What is the first term in the Fibonacci sequence to contain 1000 digits?

if __name__ == "__main__":
	i=1
	fib=1
	oldfib=0
	while(len(str(fib))<1000):
		fib,oldfib = oldfib+fib,fib
		i+=1
		#print fib
	print i
