#!/usr/bin/env pytohn2

# Project Euler: problem 52 (solved)

# It can be seen that the number, 125874, and its double, 251748, contain
# exactly the same digits, but in a different order.
# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

def get_digits(num):
    digits = {}
    for i in str(num):
        if i in digits: digits[i] += 1
        else: digits[i] = 1

    #digits = set(digits)
    return digits

def shared_items(dict1, dict2):
    return set(dict1.items()) & set(dict2.items())

if __name__ == "__main__":
    dict1 = get_digits(11234)
    dict2 = get_digits(1122334455)

    print dict1
    print dict2

    #print len( set(get_digits(1234).items()) & set(get_digits(122334455).items()) )
    save_i = 0
    for i in xrange(125874,1<<32):
        if(i%1000==0): print i
        save_i = i
        orig_digits = get_digits(i)
        tmp_i = i
        good = True
        for j in xrange(6-1):
            tmp_i += i
            if( len(shared_items(orig_digits, get_digits(tmp_i))) != len(orig_digits) ):
                good = False
                break
        if good: break

    if good:
        print "ans",save_i
        tmp_i = save_i
        for i in xrange(6-1): # this loop just prints out n..6n
            break
            tmp_i += save_i
            print tmp_i



        #len(shared_items( dict1 , dict2 ) )
