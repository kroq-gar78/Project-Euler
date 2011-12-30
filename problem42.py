#!/usr/bin/env python

# Project Euler
# http://projecteuler.net/problem=42

# Problem 42
# Using "problem42_data.txt" containing nearly two-thousand common
# English words, how many are triangle words?

def is_trinum(n):
	x=(8*n+1)**(0.5)
	#print x
	return int(x)==x

def sum_letters(x):
	x=x.strip('"').lower()
	letters="abcdefghijklmnopqrstuvwxyz"
	letter_sum=0
	for c in x:
		letter_sum+=letters.index(c)+1
	return letter_sum
	
if __name__ == "__main__":
	f=open('problem42_data.txt','r')
	words=f.read()
	words=words.split(',')
	triwords=0
	for i in words:
		if is_trinum(sum_letters(i)):
			triwords+=1
	print triwords
