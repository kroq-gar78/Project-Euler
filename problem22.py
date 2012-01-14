#!/usr/bin/env python

# Project Euler
# http://projecteuler.net/problem=22

# Problem 22
# Working out the alphabetical value for each name, using the text file
# "problem22_data.txt", multiply its value by its alphabetical position
# in the list to obtain a name score.
#
# What is the total of all the name scores in the file?

def sum_letters(x):
	x=x.strip('"').lower()
	letters="abcdefghijklmnopqrstuvwxyz"
	letter_sum=0
	for c in x:
		letter_sum+=letters.index(c)+1
	return letter_sum


if __name__ == "__main__":
	f=open("problem22_data.txt",'r')
	names=f.read()
	names=names.split(",")
	for i in xrange(len(names)):
		names[i]=names[i].strip('"').strip("'").lower()
	names=sorted(names)
	total=0
	for i in xrange(len(names)):
		total+=(i+1)*sum_letters(names[i])
	print total
