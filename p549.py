#!/usr/bin/env python2
# -*- encoding: UTF-8 -*-

# Project Euler: problem 549
# https://projecteuler.net/problem=549

# The smallest number m such that 10 divides m! is m=5.
# The smallest number m such that 25 divides m! is m=10.
#
# Let s(n) be the smallest number m such that n divides m!.
# So s(10)=5 and s(25)=10.
# Let S(n) be ∑s(i) for 2 ≤ i ≤ n.
# S(100)=2012.
#
# Find S(10^8).

import math
import Queue

def factorize(n):
    factorization = {}
    factor = 0
    for i in primes:
        if(n%i==0):
            factor=i
            break
    # if factor==0:
        # for i in xrange(primes[len(primes)-1],int(math.sqrt(n))+1):
            # ifprime = True
            # for j in primes:
                # if i%j==0:
                    # ifprime = False
                    # break
            # if ifprime:
                # if(n%i==0):
                    # factor=i
                    # break
                # if(not i in primes): primes.append(i)
        # if factor==0: return {n:1}

    exp=0
    while(n%factor==0):
        exp+=1
        n/=factor
    factorization[factor]=exp
    if(n!=factor and n!=1):
        results=factorize(n)
        for i in results.keys():
            factorization[i]=results[i]
    return factorization

primes = []

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
                # dm = divmod(tmp, a)
                # # print a, tmp, dm
                # while dm[1] == 0:
                    # exp += 1
                    # tmp = dm[0]
                    # dm = divmod(tmp, a)
                while tmp%a == 0:
                    exp += 1
                    tmp //= a
                sieve[n][a] = exp
            sieve[a] = {a: 1}
    sieve[1] = {1: 1}

    return sieve

if __name__ == "__main__":
    # prime sieve
    # target = 84
    target = 10**8
    # s = fac_sieve(target)

    primes = sieve(target)
    # primes = filter(lambda x: len(x)==1 and x.items()[0][1] == 1 and x.items()[0][0] > 1, s)
    # print sieve
    print "Finished generating primes"
    print len(primes)

    maxs = [0, 0] + [0]*(target-2+1) # s(x) = maxs[x]
    # print "len",len(maxs)
    log_target = math.log(target)
    max_p_exp = 0
    for p in primes:
        denoms = [p] # denominators
        next_p_exp = denoms[0]*p # next denominator
        sol = p
        for k in xrange(1, int(math.ceil(log_target/math.log(p))+1)):
            p_k = p**k

            # calculate x = s(p^k)
            # k = x/p + x/(p^2) + x/(p^3) + ...
            # by adding more terms until LHS <= RHS and x < p^n
            for x in xrange(sol, p*k+1, p):
                if x >= next_p_exp:
                    # p_exp *= p
                    # nmrtr = (nmrtr*p)+1
                    # next_p_exp *= p
                    # next_nmrtr = (next_nmrtr*p)+1
                    denoms.append(next_p_exp)
                    next_p_exp *= p
                    # max_p_exp = max(max_p_exp, math.log(p_exp, p))
                if k <= sum(map(lambda d: x/d, denoms)):
                    sol = x
                    # if p_k == 4096: print "sol",p,k,x,denoms
                    break

            # tmp = p*k
            # exp = 1
            # sol = asdf

            for i in xrange(1, target/p_k + 1):
                if i%p == 0: continue # if it's divisible, it would effectively add to `k`, messing up `sol`
                idx = p_k*i
                # if idx==4096:
                    # print "ASDF"
                    # print p,k,i
                maxs[idx] = max(maxs[idx], sol)

    # print range(0, target+1)
    # print maxs
    print sum(maxs)
