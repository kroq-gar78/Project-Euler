#!/usr/bin/env python

# Project Euler: problem 31
# http://projecteuler.net/problem=31

# Solution: recursive. There's probably a better implementation of this out there.

def change(coins,amt):
	ret = 0
	tmp_amt = round(amt,2)
	#print coins,amt
	if(tmp_amt<0): return 0
	if(tmp_amt>0 and len(coins)==0): return 0
	#if(amt==0 and len(coins)==0): return 1
	if(tmp_amt==0 and len(coins)==0):
		#print "two zeroes"
		return 1
	if(len(coins)==0): return 0
	if(len(coins)==1 and tmp_amt!=0 and tmp_amt<coins[-1]):
		#print "line14",coins,amt,0
		return 0
	#if(amt<=0 or len(coins)==0): return 1
	#if(len(coins)==1): return int(amt/coins[0])
	#if(round(amt,2)==coins[0]): ret+=1
	maxcoins = (float(amt)-amt%coins[0])/coins[0]
	#print maxcoins*coins[0]
	for i in xrange(0,int(maxcoins)+2):
		ways=change(coins[1:],amt-i*coins[0])
		ret+=ways
		#print coins[1:],amt-i*coins[0],ways
		#print ret
	return ret

if __name__=="__main__":
	amt=2.0
	amt+=0.00000000001 # to work around precision loss during % function
	coins=[2.0,1.0,0.5,0.2,0.1,0.05,0.02,0.01]
	#coins=[0.02,0.01]
	#coins.reverse()
	print change(coins,amt)
	
