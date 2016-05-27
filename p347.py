#!/usr/bin/env python2

# Project Euler: problem 347
# https://projecteuler.net/problem=347

import math
import Queue

if __name__ == "__main__":
    primes = [2]
    N = int(1e7)
    for i in xrange(3,(N)/2,2):
        if (i+1)%int(1e6)==0: print i+1
        isprime=True
        sqrt_i = math.sqrt(i)
        for j in primes:
            if i%j==0: isprime=False; break
            if j >= sqrt_i: break
        if isprime: primes.append(i)
    print len(primes)
    print "Done generating primes"

    M = {}
    ans = 0
    for i in xrange(len(primes)-1):
        for j in xrange(i+1,len(primes)):
            if primes[i]*primes[j] > N: break
            q = Queue.PriorityQueue()
            q.put(primes[i]*primes[j])
            old, tmp = 0, 0
            while not q.empty():
                old, tmp = tmp, q.get()
                if tmp > N:
                    # print primes[i], primes[j], old
                    # M[(primes[i],primes[j])] = old
                    ans += old
                    break
                q.put(tmp*primes[i])
                q.put(tmp*primes[j])
            # if primes[i]*primes[j]
    # print sum(v for k,v in M.items())
    print ans
