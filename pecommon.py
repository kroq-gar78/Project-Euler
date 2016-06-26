#!/usr/bin/env python2
# -*- encoding: UTF-8 -*-

# common functions/utilities for Project Euler solutions

import math

# concatenate list into a string
# NOTE: untested
def cat(a):
    return ''.join(map(str, a)) # cast to string for safety

# Euclidean GCD algorithm
def gcd(a,b):
	while b: a,b = b,a%b
	return a

# prime sieve up through `n`
def sieve(target):
    sieve = [0, 0] + range(2, target+1) # keep elements as ints until factorized
    for a in sieve:
        if a>0:
            for i in xrange(a<<1, target+1, a):
                sieve[i] = 0

    return filter(None, sieve)

# factorize all numbers through `n` using a sieve
def fac_sieve(target):
    sieve = [{}, {}] + range(2, target+1) # keep elements as ints until factorized
    for i,a in enumerate(sieve):
        if isinstance(a, int) and a>0:
            for n in xrange(a<<1, target+1, a):
                if isinstance(sieve[n], int):
                    sieve[n] = {}
                exp = 0
                tmp = n
                while tmp%a == 0:
                    exp += 1
                    tmp //= a
                sieve[n][a] = exp
            sieve[a] = {a: 1}
    sieve[1] = {1: 1}

    # To get primes from this sieve, use the line below:
    #primes = filter(lambda x: len(x)==1 and x.items()[0][1] == 1 and x.items()[0][0] > 1, s)

    return sieve
