#!/usr/bin/env python

# 
# Project Euler
#

# Problem 45
# Triangle number = n(n+1)/2
# Pentagonal number = n(n+1)/2
# Hexagonal number = n(2n-1)
# Find the next triangle number that is also pentagonal and hexagonal
# after 40755.

def istrinum(n):
	x=(8*n+1)**(0.5)
	#print x
	return int(x)==x
def ispentnum(n):
	x=((24*n+1)**(0.5)+1)/6
	#print x
	return int(x)==x
def ishexnum(n):
	x=((8*n+1)**(0.5)+1)/4
	#print x
	return int(x)==x

if __name__ == "__main__":
	i=40756
	# all hexnums are trinums, so no need to check for trinums
	while True:
		#trin=istrinum(i)
		#pentn=ispentnum(i)
		#hexn=ishexnum(i)
		#print i
		if ispentnum(i)==True:
			if ishexnum(i)==True:
				print i; exit()
			else: i+=1; continue
		else: i+=1; continue
		if trin==False or pentn==False or hexn==False:
			i+=1
		if trin==True and pentn==True and hexn==True: print i; exit()
		
	print istrinum(i)
	print ispentnum(i)
	print ishexnum(i)
	print i
