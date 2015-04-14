#!/usr/bin/env python

# Project Euler: problem 18
# https://projecteuler.net/problem=18

# Find the maximum total path sum from top to bottom of the triangle below [stored in "problem18_data.txt"]

# used dynamic programming to calculate the maximum path sums from bottom to top

if __name__ == "__main__":
    f = open('problem18_data.txt','r')
    lines = map(lambda x: x.strip(), f.readlines())
    tri = []
    for i in lines: # convert lines to integers
        tri.append(map( lambda x: int(x), i.split() ))
    
    #tri = [[3],[7,4],[2,4,6],[8,5,9,3]] # test case
    
    dp = tri
    #tmp = []
    #for i in xrange(len(tri)): # set last row equal to row original triangle
    #    tmp.append(i)
    for i in reversed(xrange(0,len(tri)-1)): # don't redo the bottom row
        #print i
        for j in xrange(i+1):
            print i,j
            dp[i][j] += max( dp[i+1][j] , dp[i+1][j+1] )
    print dp[0][0]
