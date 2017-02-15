#!/usr/bin/env python2

# Project Euler: problem 301
# https://projecteuler.net/problem=301

if __name__ == "__main__":
    ans = 0
    for n in xrange(1, (1<<30)+1):
        n_2 = n<<1
        if(( n ^ (n<<1) ^ (n+n_2) ) == 0):
            ans += 1
            if( n == 1): print "yes"
    print ans
