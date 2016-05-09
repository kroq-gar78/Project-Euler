#!/usr/bin/env python2

# Project Euler: problem 63
# https://projecteuler.net/problem=63

import math

def num_digits(n):
    return len(str(n))

if __name__=="__main__":

    ans = 0
    for a in xrange(1,10):
        print math.log(10)/math.log(10./a)
        ans += int(math.log(10)/math.log(10./a))
        # for n in xrange(1,math.floor(math.log(10)/math.log(10./a)+1)):
            # print a, n, int(math.floor(math.log(a**n, 10)))+1
            # ans +=1
            # if int(math.floor(math.log(a**n, 10)))+1 == n:
                # print "yes", a, n
    print ans
