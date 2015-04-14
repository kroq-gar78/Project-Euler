#!/usr/bin/env python

# Project Euler

# Problem 40
# http://projecteuler.net/problem=40

# An irrational decimal fraction is created by concatenating the
# positive integers: 0.123456789101112131415161718192021...
# If d(n) represents the nth digit of the fractional part, find the value
# of the following expression d(1) * d(10) * d(100) * d(1000) *
# d(10000) * d(100000) * d(1000000)

if __name__ == "__main__":
	frac = ""
	for i in xrange(1,1000000):
		frac += str(i)
	print int(frac[0])*int(frac[9])*int(frac[99])*int(frac[999])*int(frac[9999])*int(frac[99999])*int(frac[999999])
