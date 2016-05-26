#!/usr/bin/env python

# Project Euler: Problem 187
# http://projecteuler.net/problem=187

# How many composite integers, n < 10^8, have precisely two, not
# necessarily distinct, prime factors?
#
# Examples are 4, 6, 9, 10, 14, 15, 21, 22, 25, and 26.

import math

if __name__ == "__main__":
    # load primes from files since it takes too long
    # primes from: https://primes.utm.edu/lists/small/millions/
    from zipfile import ZipFile
    primes = []
    for i in xrange(1,5+1):
        f = ZipFile('primes%d.zip' % i)
        lines = f.read('primes%d.txt' % i).split('\n')
        # ugly, but it works
        primes += map(int,
                      (item for sublist in (x.split() for x in lines[2:]) for item in sublist))
    print "Done loading primes"
    # print len(primes), primes[0]

    max_val = 10**8
    # max_val = 200000
    ans = 0
    for i,a in enumerate(primes):
        # if i%10000==0: print i
        if a>max_val: break
        for b in primes:
            if b>a or a*b > max_val: break
            else:
                # print a,b,a*b
                ans += 1
    print ans
