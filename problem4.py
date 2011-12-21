#!/usr/bin/env python

def isPalindrome(n): # 6 digit palindromes only
	string = str(n)
	return (string[0]==string[5] and string[1]==string[4] and string[2]==string[3])

if __name__ == "__main__":
	answer = 0
	candidates = []
	for i in xrange(100000,999999):
		if isPalindrome(i):
			for j in xrange(100,999):
				if i%j==0:
					if(len(str(i/j))==3): candidates.append(i)
	print candidates[len(candidates)-1]
