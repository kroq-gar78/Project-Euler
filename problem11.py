#!/usr/bin/env python

# Project Euler

# Problem 11
# http://projecteuler.net/problem=11

# What is the greatest product of four adjacent numbers in any direction
# (up, down, left, right, or diagonally) in the 20x20 grid (stored in file 
# 'problem11_data.txt')?

if __name__ == "__main__":
	data = open('problem11_data.txt','r')
	grid = data.readlines()
	for i in xrange(len(grid)):
		grid[i] = grid[i].split(' ')
		for j in xrange(len(grid[i])):
			grid[i][j] = int(grid[i][j]) # cast all from string to int
	
	# brute force the solution
	largest = 0
	
	# do left/right
	for i in xrange(len(grid)):
		for j in xrange(len(grid[i])-3):
			multiplied = grid[i][j]*grid[i][j+1]*grid[i][j+2]*grid[i][j+3]
			if( multiplied > largest ):
				largest = multiplied
	for i in xrange(len(grid)-3):
		# do up/down
		for j in xrange(len(grid[i])):
			multiplied = grid[i][j]*grid[i+1][j]*grid[i+2][j]*grid[i+3][j]
			if( multiplied > largest ):
				largest = multiplied
		# do diagnally (top to bottom)
		for j in xrange(len(grid[i])-3):
			multiplied = grid[i][j]*grid[i+1][j+1]*grid[i+2][j+2]*grid[i+3][j+3]
			if( multiplied > largest ):
				largest = multiplied
		# do diagnally (bottom to top)
		for j in xrange(len(grid[i])-3):
			multiplied = grid[i][j+3]*grid[i+1][j+2]*grid[i+2][j+1]*grid[i+3][j]
			if( multiplied > largest ):
				largest = multiplied
	print largest
	
	#i=6
	#j=8
	
	#multiplied = grid[i][j]*grid[i+1][j+1]*grid[i+2][j+2]*grid[i+3][j+3]
	#if( multiplied > largest ):
	#largest = multiplied
	#print largest
	#print grid[i][j],grid[i+1][j],grid[i+2][j],grid[i+3][j]
	
	
			
	
		
			
