#!/usr/bin/env python2

# Project Euler: problem 203
# http://projecteuler.net/problem=203

# Solution: generate Pascal's triangle up to the 51st row (including the
# first), then look at the distinct numbers and see how many are square-free
# (using trial division)

# program modeled after solution for problem 53 (`p053.py`)

import math

if __name__=="__main__":
    # calculate triangle
    n = 51
    nums = set([1]) # distinct numbers from the Triangle
    pascal = [[1]+[0]*(n-1)]
    #print pascal
    for i in xrange(1,n):
        row=[0]*n
        row[0]=1
        row[i]=1
        if(i>1):
            for j in xrange(1,i):
                row[j]=pascal[i-1][j-1]+pascal[i-1][j]
                nums.add(row[j])
        #print row
        pascal.append(row)
    #print pascal

    # generate primes
    primes = []
    for i in xrange(3,math.ceil(math.sqrt(max(nums)))+1,2):
        if (i+1)%int(1e6)==0: print i+1
        isprime=True
        sqrt_i = math.sqrt(i)
        for j in primes:
            if j > sqrt_i: break
            if i%j==0: isprime=False; break
        if isprime:
            primes.append(i)
    primes.insert(0,2) # cheap trick to get rid of some computations
    print "Finished generating primes"

    # test for squarefree numbers
    primes_sq = [x*x for x in primes]
    ans = 0
    for i in nums:
        sqfree = True
        for j in primes_sq:
            if i < j: break
            if i%j==0:
                sqfree = False
                break
        if sqfree:
            ans += i
            print i

    print ans
