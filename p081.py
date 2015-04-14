#!/usr/bin/env python

# Project Euler: problem 81 (SOLVED)
# https://projecteuler.net/problem=81

# In the 5 by 5 matrix below, the minimal path sum from the top left to the
# bottom right, by only moving to the right and down, is indicated in bold red
# [marked with '*'] and is equal to 2427.

# 131* , 673 , 234  , 103  , 18
# 201* , 96* , 342* , 965  , 150
# 630  , 803 , 746* , 422* , 111
# 537  , 699 , 497  , 121* , 956
# 805  , 732 , 524  , 37*  , 331*

# Find the minimal path sum, in matrix.txt [saved as 'p081_data.txt'],
# a 31K text file containing a 80 by 80 matrix, from the top left to
# the bottom right by only moving right and down.

if __name__ == "__main__":
    # first use the example array
    #array = ["131 673 234 103 18",
    #         "201 96  342 965 150",
    #         "630 803 746 422 111",
    #         "537 699 497 121 956",
    #         "805 732 524 37  331"]
    #array = ["1 2", "3 4"]

    f = open('p081_data.txt','r')
    array = f.readlines()
    array = [map(int,x.split(",")) for x in array]

    # use dynamic programming to calculate minimum path sums from top to bottom
    dp = [[0]*len(x) for x in array] # array of 0's, same size as 'array'

    dp[0][0] = array[0][0]
    for i in xrange(len(dp)):
        for j in xrange(len(dp[i])):
            #print i,j
            if(i==0): # on first row
                if(j==0): continue
                dp[i][j] = dp[i][j-1] + array[i][j]
                #print i,j, dp
            elif(j==0): # on first column
                dp[i][j] = dp[i-1][j] + array[i][j]
                #print i,j,dp
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + array[i][j]
                #print i,j,dp

    print dp[-1][-1]

