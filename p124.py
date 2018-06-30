#!/usr/bin/env python2

# Project Euler: problem 124
# https://projecteuler.net/problem=124

import math
import operator

primes = []
primes_set = set()

def pfactors(n):
    factors = set()
    for i in primes:
        if(n < i):
            break
        if(n%i==0):
            while(n%i==0): n/=i
            factors.add(i)
            if(n==1): return factors
    if factors==[]: return [n]
    if(n != 1):
        factors.add(n)

    return factors

if __name__ == "__main__":
    # generate all primes needed to factorize all numbers up to 100,000
    N_MAX = 100000
    primes = []
    for n in xrange(2, int(math.sqrt(N_MAX))+1):
        isprime = True
        for prime in primes:
            if n%prime==0:
                isprime = False
                break
        if isprime:
            primes.append(n)
    primes_set = set(primes)

    # calculate rad(n) for all numbers. `i`th index is rad(i)
    rad = [0]*(N_MAX + 1)
    rad[0] = 0
    rad[1] = 1
    for n in xrange(2, N_MAX+1):
        rad[n] = reduce(operator.mul, pfactors(n))

    ordered = sorted(enumerate(rad), key=lambda x: x[1])
    E = lambda x: ordered[x][0]
    print E(10000)
