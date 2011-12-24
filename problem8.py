#!/usr/bin/env python

# 
# Project Euler
#

# Problem 8
# Find the greatest product of five consecutive digits in the
# 1000-digit number (in data file "problem8_data.txt")

if __name__ == "__main__":
	number=open("problem8_data.txt",'r').readline()
	digitproducts=[]
	for i in reversed(range(5)):
		if str(i*(i+1)*(i+2)*(i+3)*(i+4)) in number:
			print i
			print i*(i+1)*(i+2)*(i+3)*(i+4)
			exit()
		
