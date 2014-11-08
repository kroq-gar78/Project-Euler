#!/usr/bin/env python

# 
# Project Euler
#

# Problem 80
# For the first one hundred natural numbers, find the total of the
# digital sums of the first one hundred decimal digits for all the
# irrational square roots.

import decimal

def isPerfectSquare(n):
	sqrt = int(n)**0.5
	return n == sqrt**2

def digisum(n):
	#print n
	answer = str(decimal.Decimal(n).sqrt())
	'''print (str(answer[answer.index('.')+1:]))
	#while( len(str(answer[answer.index('.')+1:])) < 100 ):
	while(len(str(answer))-1 < 101):
		decimal.getcontext().prec += 1
		answer = str(decimal.Decimal(n).sqrt())
		print n
	#while( len(str(answer[answer.index('.')+1:])) > 100 ):
	while(len(str(answer))-1 > 101):
		decimal.getcontext().prec -= 1
		answer = str(decimal.Decimal(n).sqrt())
		print answer
	print decimal.getcontext().prec'''
	#n=str(answer[answer.index('.')+1:])
	n = str(answer).replace(".","")[:100]
	print n
	#if '.' in n:
	#	n = n.replace('.','0')
		#n=str(n[n.index('.')+1:])
		#print len(n)
		#print n
	#else: return 0
	if(int(n)==0): return 0
	ret=0
	for i in n:
		#print i
		ret+=int(i)
		#print ret
	return ret
	
if __name__ == "__main__":
	# digits left AND right of the decimal... derp...
	decimal.getcontext().prec = 102
	total=0
	squares=set(i*i for i in range(2,10))
	
	for i in xrange(2,100):
		if i in squares: continue
		n = str(int(decimal.Decimal(i).sqrt()*10**99))
		total+=sum(int(c) for c in n)
	
	
	#i=2
	#answer = str(decimal.Decimal(i).sqrt())
	#print len(i)
	#while( len(str(answer[answer.index('.'):])) < 100 ):
	#	decimal.getcontext().prec += 1
	#	answer = str(decimal.Decimal(i).sqrt())
	#print digisum(2)
	#print isPerfectSquare(100)
	'''for i in xrange(2,100):
		if isPerfectSquare(i): continue
		#sqrt = decimal.Decimal(i).sqrt()
		#sqrt = str(sqrt)
		#if i==3: print sqrt
		#if i==4: print sqrt
		#if not isPerfectSquare(i):
		#	if i==4: print "fail"
		#	decimal.getcontext().rec = 100
			#while( len(str(sqrt[sqrt.index('.')+1:])) < 100 ):
			#	decimal.getcontext().prec += 1
			#	sqrt = str(decimal.Decimal(i).sqrt())
		#	total += digisum(sqrt)
		#else:
		#	if i==9: print sqrt
		total+=digisum(i)
		print i'''
	#total = digisum(decimal.Decimal(2).sqrt())
	print total
