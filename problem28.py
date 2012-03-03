#!/usr/bin/env python

# Project Euler
# Problem 28
# http://projecteuler.net/problem=28

# Starting with the number 1 and moving to the right in a clockwise
# direction a 5 by 5 spiral is formed as follows:

# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13

# What is the sum of the numbers on the diagonals in a 1001 by 1001
# spiral formed in the same way?

def printSpiral(spiral):
	for line in spiral:
		#print line
		string = ""
		for j in line:
			string += ("%04d" % int(j)) + "  "
		print string

def genSpiral(len):
	print "Not yet implemented."

if __name__ == "__main__":
	spiral=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
	
	# MIDDLE INDEX = (len(spiral)-1)/2
	
	up = [-1,0]
	down = [1,0]
	left = [0,-1]
	right = [0,1]
	
	i = (len(spiral)-1)/2
	j = (len(spiral)-1)/2
	number = 1
	stepsNeeded = 1
	stepsLeft = 1
	repsLeft = 2 # reps needed is always 2
	direction = right
	while( not (i == 0 and j == 5) ):
		print "Index: " + ("[%d][%d]" % (i,j))
		spiral[i][j] = number
		number += 1
		i += direction[0]
		j += direction[1]
		stepsLeft -= 1
		if( stepsLeft == 0 ):
			print "No steps left"
			# set new direction
			if( direction == up ): direction = right
			elif( direction == down ): direction = left
			elif( direction == left ): direction = up
			elif( direction == right ): direction = down
			
			# process repetitions
			repsLeft -= 1
			if( repsLeft == 0 ):
				print "2 reps over"
				repsLeft = 2
				stepsNeeded += 1
			stepsLeft = stepsNeeded
	
	printSpiral(spiral)
	#print spiral
