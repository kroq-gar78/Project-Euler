#!/usr/bin/env python

# Project Euler: problem 99

# Using base_exp.txt [renamed to 'problem99_data.txt'], a 22K text file
# containing one thousand lines with a base/exponent pair on each line,
# determine which line number has the greatest numerical value.

import math

if __name__ == "__main__":
	datafile = file('problem99_data.txt','r')
	lines = datafile.readlines()
	
	largestline = 0
	largestval = 0
	for i in xrange(len(lines)):
		# parse file
		pair = lines[i].split(",")
		for j in xrange(len(pair)): pair[j] = int(pair[j])
		# use logs to calculate value; will be b*ln(a)
		val = pair[1]*math.log(pair[0])
		if(val>largestval):
			largestline = i+1
			largestval = val
	print largestline
