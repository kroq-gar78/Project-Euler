#!/usr/bin/env python

# Project Euler
# http://projecteuler.net/problem=26

# Problem 26
# Find the value of d < 1000 for which 1/d contains the longest
# recurring cycle in its decimal fraction part.

# divide() taken from http://www.nerdparadise.com/tech/python/repeatingdecimaldivision/
def divide(numerator, denominator, detect_repetition=True, digit_limit=None):

    # If repetition detection is off, you must
    # specify a limit on the digits returned
    if not detect_repetition and digit_limit == None:
        return None

    decimal_found = False
    
    v = numerator // denominator
    numerator = 10 * (numerator - v * denominator)
    answer = str(v)
    
    if numerator == 0:
        return answer
    
    answer += '.'
    
    # Maintain a list of all the intermediate numerators
    # and the length of the output at the point where that
    # numerator was encountered. If you encounter the same
    # numerator again, then the decimal repeats itself from
    # the last index that numerator was encountered at.
    states = {}
    
    while numerator > 0 and (digit_limit == None or digit_limit > 0):
        
        if detect_repetition:
            prev_state = states.get(numerator, None)
            if prev_state != None:
                start_repeat_index = prev_state
                non_repeating = answer[:start_repeat_index]
                repeating = answer[start_repeat_index:]
                return len(repeating)
                #return non_repeating + '[' + repeating + ']'
            states[numerator] = len(answer)
        
        v = numerator // denominator
        answer += str(v)
        numerator -= v * denominator
        numerator *= 10
        if digit_limit != None:
            digit_limit -= 1
    
    if numerator > 0:
        return answer + '...'
    return 0

if __name__ == "__main__":
	mostrep=1
	num=1
	for d in xrange(1,1000):
		replength=int(divide(1,d))
		print int(replength)>int(mostrep)
		if (replength > mostrep):
			print mostrep,d
			mostrep=replength
			num=d
	print num
