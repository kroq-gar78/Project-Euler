#!/usr/bin/env python

# Project Euler: problem 53
# http://projecteuler.net/problem=53

# Solution: generate Pascal's triangle up to the 101st row (including the
# first), then go back and count how many are above 1,000,000

if __name__=="__main__":
	n = 101
	pascal = [[1]+[0]*(n-1)]
	#print pascal
	for i in xrange(1,n):
		row=[0]*n
		row[0]=1
		row[i]=1
		if(i>1):
			for j in xrange(1,i):
				row[j]=pascal[i-1][j-1]+pascal[i-1][j]
		#print row
		pascal.append(row)
	#print pascal
	
	ans = 0
	
	for i in pascal:
		for j in xrange(1,(len(i))):
			if(i[j]>1000000): ans += 1
	print ans
