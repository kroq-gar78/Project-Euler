#!/usr/bin/env python2

# Project Euler: Problem 500
# https://projecteuler.net/problem=500

import itertools
import math
import operator

if __name__ == "__main__":
    target = 500500
    mod = 500500507
    #target = 15
    primes = []
    for i in itertools.count(3,step=2): # basically, an unbounded xrange
        if (i+1)%int(1e6)==0: print i+1
        isprime=True
        sqrt_i = math.sqrt(i)
        for j in primes:
            if i%j==0: isprime=False; break
            if j >= sqrt_i: break
        if isprime:
            primes.append(i)
            if len(primes)+1 >= target: break
    primes.insert(0,2) # cheap trick to get rid of some computations
    print len(primes)
    primes_log = [math.log(x,2) for x in primes] # I wish pypy supported numpy
    print "Done generating primes"

    # where `x` is the diff between the old and new exponent on 2
    log_2 = math.log(2)
    exp = [1] # exponents of each prime
    diff = [1<<1] # diff between current and new exponent
    logs = [2] # precomputed logs for each prime**diff (except for 2, since it can be huge)
    # diff = [1<<(target-1)] # diff between current and new exponent; for power of 2, it goes down
    count_divisors = lambda l: reduce(operator.mul, (x+1 for x in l)) # shortcut function
    # print exp, diff
    # min_val = 1<<first_exp
    # current_val = min_val
    curr_prime = 0 # index in `primes`
    current_val = 1

    for i in xrange(1,target):
        if i%10000==0: print i

        inc = False # have we done anything in the loop?
        idx = logs.index(min(logs)) # canditate to increment
        #idx, _ = min(enumerate(logs), key=operator.itemgetter(1))

        #print i, primes[idx], logs[idx], primes_log[curr_prime+1]
        #print logs

        if logs[idx] < primes_log[curr_prime+1]: # check if 1) would decrease number, and 2) is better than adding a new prime
            #if (1<<diff[0]) > primes[i]**diff[i]:
            # print "Increase exp on", primes[i]
            exp[idx] += diff[idx]
            diff[idx] <<= 1
            logs[idx] = diff[idx]*primes_log[idx]
            inc = True
            #print "inc",primes[idx]
            #print logs

        if not inc:
            # print "Add prime:", primes[curr_prime+1]
            exp.append(1)
            diff.append(2)
            logs.append(2*primes_log[curr_prime+1])
            curr_prime += 1
            #print exp, diff


    # print exp
    # print diff
    # print count_divisors(exp)
    print "Calculating answer..."
    ans = 1
    for i in xrange(len(exp)):
        #ans *= pow(primes[i],exp[i])
        ans *= pow(primes[i],exp[i],mod)
        ans %= mod
    print ans
