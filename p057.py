#!/usr/bin/env python2

# Project Euler: problem 57
# https://projecteuler.net/problem=57

# TODO: paste problem statement later

import math
from pecommon import gcd

# get the nth iteration of the infinite continued fraction of sqrt(2)
# where (1 + 1/2 = 3/2) is when n=1
# my observation is that gcd(top,bot) always = 1, but not sure
def sqrt2_covgt(n):
    assert n>0

    top = 1 # numerator
    bot = 2 # denominator

    for i in xrange(n-1):
        top += bot*2 # add 2 for all but the 0th "term"
        top, bot = bot, top # reciprocal

    top += bot
    return top, bot

if __name__ == "__main__":
    # target = 1000
    target = 1000


    ans = 0
    log_10 = math.log(10)
    digits_base10 = lambda x: int(math.floor(math.log(x)/log_10))+1
    for i in xrange(1,target+1):
        top,bot = sqrt2_covgt(i)
        if digits_base10(top) > digits_base10(bot):
            ans += 1
    print ans
