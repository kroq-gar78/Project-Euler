#!/usr/bin/env python

# Project Euler
# http://projecteuler.net/problem=24

# Problem 24
# What is the millionth lexicographic permutation of the digits
# 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9 after being numerically ordered?

def nextIndex(i,x): # i is index, x is positive offset; length hard-coded to be 10
	return (i+x)%10

if __name__ == "__main__":
	perms=[]
	digits=[0,1,2,3,4,5,6,7,8,9]
	
	for i in digits:
		num=i*1000000000
		print i,digits
		digitsj=digits.remove(i)
		print digitsj
		for j in digitsj:
			num+=j*100000000
			digitsk=digitsj.remove(j)
			for k in digitsk:
				num+=k*10000000
				digitsl=digitsk.remove(k)
				for l in digitsl:
					num+=l*1000000
					digitsm=digitsl.remove(l)
					for m in digitsm:
						num+=m*100000
						digitsn=digitsm.remove(m)
						for n in digitsn:
							num+=n*10000
							digitso=digitsn.remove(n)
							for o in digitso:
								num+=o*1000
								digitsp=digitso.remove(o)
								for p in digitsp:
									num+=p*100
									digitsq=digitsp.remove(p)
									for q in digitsq:
										digitsr=digitsq.remove(q)
										perms.append(num+q*10+digitsq.remove(q)[0])
											
	
	print perms[1000000]
