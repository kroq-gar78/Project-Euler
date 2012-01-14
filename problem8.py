#!/usr/bin/env python

# Project Euler
# http://projecteuler.net/problem=8

# Problem 8
# Find the greatest product of five consecutive digits in the 1000-digit
# number (in file "problem8_data.txt").

if __name__ == "__main__":
	number=str(int(open("problem8_data.txt",'r').read())) # str to int to str removes any extra formatting
	greatest=0
	for i in xrange(len(number)-5):
		product=int(number[i])*int(number[i+1])*int(number[i+2])*int(number[i+3])*int(number[i+4])
		print product
		print int(number[i]),int(number[i+1]),int(number[i+2])
		if product>=greatest: # huh???? why syntax error??? FOUND YA!
			greatest=product
	print greatest # silly me
