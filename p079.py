#!/usr/bin/env python2

# Project Euler: problem 79
# https://projecteuler.net/problem=79


# A common security method used for online banking is to ask the user for three
# random characters from a passcode. For example, if the passcode was 531278,
# they may ask for the 2nd, 3rd, and 5th characters; the expected reply would
# be: 317.

# The text file, keylog.txt [saved as 'p079_keylog.txt'], contains fifty
# successful login attempts.

# Given that the three characters are always asked for in order, analyse the
# file so as to determine the shortest possible secret passcode of unknown
# length.

import itertools

def isValid(combo, rules):
    # print rules
    for r in rules:
        if len(combo) < len(r):
            return False
        start = 0
        good = True
        for c in r:
            c = int(c)
            # print "start",start
            for i in xrange(start, len(combo)):
                combo_i = int(combo[i])
                if combo_i == c:
                    # print "asdf",i,combo[i],c,r
                    start = i+1
                    break
            if combo_i != c:
                # print i,combo[i],c,r
                return False
    return True

if __name__ == "__main__":
    f = open('p079_keylog.txt', 'r')
    rules = [x.strip() for x in f.readlines()]
    rules = list(set(rules))

    combo = ''.join(rules)
    print "orig",len(combo)
    i = 0
    while (i) < len(combo):
        combo_tmp = '%s' % combo # janky string copy
        combo_tmp = combo_tmp[:i] + combo_tmp[(i+1):]
        # print "len",len(combo),len(combo_tmp)
        if isValid(combo_tmp, rules):
            combo = combo_tmp
        else:
            i += 1

    # this gives an upper bound for the length of the answer, since this is kind
    # of a greedy algorithm
    # print "out",len(combo)
    print "upper bound",len(combo)
    # print combo # solution of upper bound

    # search below the upper bound
    for i in xrange(1,len(combo)):
        print "len =",i
        for c in itertools.product(range(10), repeat=i):
            l = list(c)
            # if isValid(''.join(map(str,l)), rules):
            if isValid(l, rules):
                print ''.join(map(str,l))
                exit(0)
