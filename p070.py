#!/usr/bin/env python2

# Project Euler: problem 70
# https://projecteuler.net/problem=70

from bisect import bisect_left
import collections
import math
import time

# from: https://stackoverflow.com/a/2233940
def binary_search(a, x, lo=0, hi=None):   # can't use a to specify default for hi
    hi = hi if hi is not None else len(a) # hi defaults to len(a)
    pos = bisect_left(a,x,lo,hi)          # find insertion position
    return (pos if pos != hi and a[pos] == x else -1) # don't walk off the end

def isPrime(n,primes=[2]):
    if(n&1==0 or n<2): return (n==2)
    for i in primes:
        if(n%i==0): return (n==i)
    for i in xrange(primes[len(primes)-1],int(math.sqrt(n))+1):
        ifprime = True
        for j in primes:
            if i%j == 0:
                ifprime = False
                break
        if ifprime:
            if n%i==0: return False
            if( not i in primes ): primes.append(i)

    #print primes

    for i in primes:
        if n%i == 0:
            return False
    return True

def pfactors(n,primes=[2]):
    # print n
    factors = set()
    for i in primes:
        if(n%i==0):
            while(n%i==0): n/=i
            factors.add(i)
            isprime = (binary_search(primes,n) >= 0)
            # print "isprime", n, isprime, binary_search(primes,n)
            if isprime and (not n in factors): factors.add(n)
            if(n==1 or isprime): return factors
            break
    # print factors, n
    # if n!=1:
        # for i in xrange(primes[len(primes)-1],n):
            # ifprime = True
            # for j in primes:
                # if i%j==0:
                    # ifprime = False
                    # break
            # if ifprime:
                # if(n%i==0):
                    # while(n%i==0): n/=i
                    # factors.append(i)
                    # isprime =binary_search(primes,n) >= 0
                    # if isprime and (not n in factors): factors.append(n)
                    # if(n==1 or isprime): return factors
                # if(not i in primes): primes.append(i)
    # if factors==[]: return [n]
    if n!=1: factors.add(n)

    return factors

def totient(n,primes=[2]):
    pfacs = pfactors(n,primes=primes)
    # print n, pfacs
    return reduce(lambda x, y: int(x*(1-1./y)), pfacs, n)

# adapted from: https://stackoverflow.com/a/396438
def isPermutation(a,b):
    if(len(a) != len(b)): return False
    d = collections.Counter()
    for i in a:
        d[i] += 1
    for i in b:
        d[i] -= 1
    return not any(d.itervalues())

if __name__ == "__main__":
    primes = [2]
    # for num in xrange(3,int(10**(7./2))):
    for num in xrange(2,(10**7)/2):
        if(isPrime(num)): primes.append(num)
    # print primes

    # print pfactors(13994, primes=primes)
    # print totient(13994, primes=primes)
    # exit(0)

    ans = -1
    min_ratio = 87109./79180 # inferred from problem statement
    for n in xrange(2,10**7):
        # if n%10000==0: print n
        # if n%4==0: continue
        phi = totient(n, primes=primes)
        if not isPermutation(str(phi), str(n)): continue
        # print "r",n
        ratio = float(n)/phi
        if(ratio < min_ratio):
            ans = n
            min_ratio = ratio
            print ans
