#!/usr/bin/env python2

# Project Euler: problem 204
# https://projecteuler.net/problem=204

# We will call a positive number a generalised Hamming number of type n, if it
# has no prime factor larger than n.
#
# How many generalised Hamming numbers of type 100 are there which don't exceed
# 10^9?

import math
import Queue

if __name__=="__main__":
    # from `p500.py`
    # target = 10**8
    target = 10**9
    # hamming_type = 5
    hamming_type = 100
    primes = []
    for i in xrange(3,hamming_type+1,2):
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

    # generate all numbers using the primes, but that do not exceed `target`
    pq = Queue.PriorityQueue()
    # for i in primes: pq.put(i)
    # n = pq.get()
    n = 1
    s = set([n])
    ans = 1
    progress = 100
    while n < target:
        if n >= progress:
            print progress
            progress *= 10
        for i in primes:
            prod = n*i
            if not (n*i in s):
                pq.put(prod)
                s.add(prod)
        n = pq.get()
        # print n
        ans += 1

    print "answer:", ans
