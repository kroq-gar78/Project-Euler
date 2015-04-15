#!/usr/bin/env python

# Project Euler: problem 65 (SOLVED)
# http://projecteuler.net/problem=65

# What is most surprising is that the important mathematical constant,
# e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...].

# The first ten terms in the sequence of convergents for e are:
# 2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, ...

# The sum of digits in the numerator of the 10th convergent is 1+4+5+7=17.

# Find the sum of digits in the numerator of the 100th convergent of the
# continued fraction for e.

from fractions import Fraction
from decimal import Decimal

def inf_frac_e(nterms,curr):
    if nterms==-1: return Fraction(2.0)
    if nterms==curr-1: return 0
    mod3 = curr%3
    #pattern = [1,2*(curr%3),1]
    if(mod3==2):
        tmp = inf_frac_e(nterms,curr+1)
        tmp2 = (curr/3+1)<<1
        #print curr, tmp, tmp2
        ret = tmp2 + Fraction(1,tmp) if (tmp!=0) else tmp2 # break loop if we have gone to enough terms
        #print "ret",ret
        return ret
    else:
        tmp = inf_frac_e(nterms,curr+1)
        tmp2 = Fraction(1.0 if curr>0 else 2.0) #pattern[mod3]
        #print curr, tmp, tmp2
        ret = tmp2 + Fraction(1,tmp) if (tmp!=0) else tmp2
        #print "ret",ret
        return ret


if __name__ == "__main__":
    #convergents = [Fraction(1,1),Fraction(3,2)]
    #k = 1
    #pattern_repeating = [1,2*k,1]
    #convergent = Fraction()
    #term = 3
    #if term == 1: print Fraction(2); exit()
    #elif term == 2: print Fraction(2)+Fraction(1); exit()
    #bottomElement = (term-2)%len(pattern_repeating)
    #origFrac = Fraction(pattern_repeating[bottomElement])
    #print Fraction(1,1)+Fraction(1,2+Fraction(1,2))
    #for i in xrange(term):
    #    if( i == term-1 ): # if last term
    #        origFrac = Fraction(2)+Fraction(1,origFrac)
    #    elif( i == 0 ):
    #        nextElement = bottomElement-1
    #        if nextElement < 0: nextElement = len(pattern_repeating)-1
    #        origFrac = Fraction(pattern_repeating[nextElement])+Fraction(1,origFrac)
    #    elif( i > 0 ):
    #        #print pattern_repeating[i%len(pattern_repeating)]
    #        origFrac = Fraction(pattern_repeating[(i-1)%len(pattern_repeating)])+Fraction(1,origFrac)
    #    #else:
    #    #    origFrac = Fraction(1)+Fraction(1,origFrac)
    #    #    print origFrac
    #    print origFrac
    #print (origFrac)
    #print convergents

    #pattern = [1,2,1] # add to the 2nd item as needed

    #print inf_frac_e(10-1,0)
    #print sum( map(int, str(inf_frac_e(10-1,0).numerator)) )
    print sum( map(int, str(inf_frac_e(100-1,0).numerator)) )


