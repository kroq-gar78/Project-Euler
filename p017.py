#!/usr/bin/env python

# Project Euler
# http://projecteuler.net/problem=17

# Problem 17
# If all the numbers from 1 to 1000 (one thousand) inclusive were
# written out in words, how many letters would be used? 
# 
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred
# and forty-two) contains 23 letters and 115 (one hundred and fifteen)
# contains 20 letters. The use of "and" when writing out numbers is in
# compliance with British usage.

def in_words(n):
	if n==0: return "zero"
	n=str(n)
	string=""
	for i in xrange(len(n)):
		digit=int(n[i])
		placevalue=len(n)-int(i)-1
		# "and" rule: if last 2 digits are >0, then use "and"
		if placevalue==1 and len(n)>2 and int(n[-2:])!=0: # add "and" if needed"; make sure rest of string !=0
			string+="and"
		if digit==1 and placevalue!=1:
			string+="one"
		elif digit==2 and placevalue!=1:
			string+="two"
		elif digit==3 and placevalue!=1:
			string+="three"
		elif digit==4 and placevalue!=1:
			string+="four"
		elif digit==5 and placevalue!=1:
			string+="five"
		elif digit==6 and placevalue!=1:
			string+="six"
		elif digit==7 and placevalue!=1:
			string+="seven"
		elif digit==8 and placevalue!=1:
			string+="eight"
		elif digit==9 and placevalue!=1:
			string+="nine"
		elif placevalue==1:
			if int(n[i:])==11:
				return string+"eleven"
			elif int(n[i:])==12:
				return string+"twelve"
			elif int(n[i:])==13:
				return string+"thirteen"
			elif int(n[i:])==14:
				return string+"fourteen"
			elif int(n[i:])==15:
				return string+"fifteen"
			elif int(n[i:])==16:
				return string+"sixteen"
			elif int(n[i:])==17:
				return string+"seventeen"
			elif int(n[i:])==18:
				return string+"eighteen"
			elif int(n[i:])==19:
				return string+"nineteen"
			elif digit==1:
				string+="ten"
			elif digit==2:
				string+="twenty"
			elif digit==3:
				string+="thirty"
			elif digit==4:
				string+="forty"
			elif digit==5:
				string+="fifty"
			elif digit==6:
				string+="sixty"
			elif digit==7:
				string+="seventy"
			elif digit==8:
				string+="eighty"
			elif digit==9:
				string+="ninety"
		if placevalue==2 and digit!=0:
			string+="hundred"
		elif placevalue==3:
			string+="thousand"
	return string

if __name__ == "__main__":
	# calculate len() of each in_words() of each number 1 through 1000
	total=0
	for i in xrange(1,1000+1): # need +1 to make inclusive of 1000
		total+=len(in_words(i))
	print total
