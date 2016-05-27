#!/usr/bin/env python2

# Project Euler: problem 59
# https://projecteuler.net/problem=59

import itertools

if __name__=="__main__":
    f = open('p059_cipher.txt')
    orig = map(int, f.read().strip().split(','))
    a = range(ord('a'),ord('z')+1)
    for c in itertools.product(a,a,a):
        xord = [0]*len(orig)
        for i in xrange(len(orig)):
            xord[i] = orig[i]^c[i%3]
        str = ''.join(map(chr, xord))[:10]
        if str[:10] == "(The Gospe":
            print c
            print sum(xord)
            break
