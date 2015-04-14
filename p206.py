#!/usr/bin/env python

# Project Euler: problem 206 (SOLVED)
# https://projecteuler.net/problem=206

# Find the unique positive integer whose square has the form
# 1_2_3_4_5_6_7_8_9_0, where each "_" is a single digit.

# NOTE: this runs _much_ faster in 'pypy' (as in, orders of magnitude)

import math

def isValid(num):
    digits = map(int,str(num))
    if(len(digits)!=19): return False
    for i in xrange(0,10):
        #print (i+1)%10, digits[i*2], i*2
        if(digits[i*2] != (i+1)%10): return False
    return True
    for i in xrange(0,10):
        print (10-i)%10, num%(10**(i*2)), 10**(i*2)
        if(num%(10**(i*2)) != (10-i)%10):
            return False
        else: num/=(10**(i*2))
    return True

if __name__ == "__main__":
    # second to last digit must be a 0 for it to be a square (because one factor
    # would be 10)

    # brute force the square root
    range_start = int(math.floor(math.sqrt(1020304050607080900)))
    #range_end = int(math.ceil(math.sqrt(10**19))) # go up to sqrt of max number
    range_end = int(math.ceil(math.sqrt(1929394959697989990))) # go up to sqrt of max number
    start = range_start # look for the first multiple of 30
    while(start%10!=0): start +=1
    #print "start", start
    #print "start,end", range_start, range_end
    counter = 0
    for i in xrange(start,range_end,10):
        counter += 1
        #if(counter%100000==0): print counter, i
        if(isValid(i*i)):
            print i
            break

