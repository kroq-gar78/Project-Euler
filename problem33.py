#!/usr/bin/env python

# Project Euler: problem 33
#
# The fraction 49/98 is a curious fraction, as an inexperienced
# mathematician in attempting to simplify it may incorrectly believe
# that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
#
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
#
# There are exactly four non-trivial examples of this type of fraction,
# less than one in value, and containing two digits in the numerator and
# denominator.
#
# If the product of these four fractions is given in its lowest common
# terms, find the value of the denominator.

from decimal import Decimal

# Euclidean GCD algorithm
def gcd(a,b):
	while b: a,b = b,a%b
	return a

if __name__ == "__main__":
    # x/y, x < y
    # x and y share a digit
    pairs = []
    for x in xrange(10,100):
        nextx = False
        if(x%10==0): continue # if it is divisible by 10; answer is trivial or 0
        for y in xrange(10,100):
            #if(x!=49 or y!=98): continue
            if(x>=y): continue
            if(y%10==0): continue
            print (x,y)
            #gcdxy = gcd(x,y)
            #if gcdxy==1: nextx = True; break
            commonfound = False
            for i in str(x):
                if i in str(y):
                    commonfound = True
                    #print "Found common: " + str(i)
                    xlist, ylist = list(str(x)), list(str(y))
                    del xlist[xlist.index(i)]
                    #print ylist.index(i)
                    del ylist[ylist.index(i)]
                    newx, newy = int((''.join(xlist))), int((''.join(ylist)))
                    #print newx, newy
                    break
            #print "made it"
            if not commonfound: continue
                #print "not found"
                #nextx = True
                #break
            #print "made it"
            #print str(Decimal(x)/Decimal(y))
            if (Decimal(x)/Decimal(y)) == (Decimal(newx)/Decimal(newy)):
                pairs.append((x,y))
                print (x,y)
        if nextx: continue
    solution = [1,1]
    for i in pairs:
        x, y = i
        solution[0] *= x
        solution[1] *= y
    gcdsolution = gcd(solution[0],solution[1])
    print (solution[0]/gcdsolution,solution[1]/gcdsolution)
