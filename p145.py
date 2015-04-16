#!/usr/bin/env python

# Projct Euler: problem 145 (SOLVED)
# https://projecteuler.net/problem=145

# Some positive integers n have the property that the sum [ n + reverse(n) ]
# consists entirely of odd (decimal) digits. For instance, 36 + 63 = 99 and 409
# + 904 = 1313. We will call such numbers reversible; so 36, 63, 409, and 904
# are reversible. Leading zeroes are not allowed in either n or reverse(n).
#
# There are 120 reversible numbers below one-thousand.
#
# How many reversible numbers are there below one-billion (10^9)?

import math

def isValid(n): # has all odd numbers
    for i in str(n):
        if int(i)&1==0: return False
    return True

def reverse(n): # asdf
    return int(str(n)[::-1])

if __name__ == "__main__":
    skip = set([])
    ans = 0
    end = (10**8)

    #skip = False
    next = 0
    #for i in xrange(1,end/2):
    for i in xrange(1,end):
        if i%100000==0:
            print i
            continue
        if i < next: continue
        #if i%10==0:
        #    continue
        #    placevalue = int(math.floor(math.log10(i)))
        #    if(5*(10**placevalue) <= i):
        #        next = 10**(placevalue+1)
        #        print i,next

        #if i%10==0: continue
        #print skip
        #idx = skip.find(i)
        if i in skip:
            #skip.pop()
            skip.remove(i)
            continue
        #print i, reverse(i)
        rev = reverse(i)
        if(isValid(i+rev)):
            #print i, rev, (i+rev)
            #skip.append(rev)
            skip.add(rev)
            ans += 2 # i != rev, since if they are equal, it won't be valid
    #for i in xrange(end/2,end):
    #    if i%10==0: continue
    #    print skip

    print ans

