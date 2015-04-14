#!/usr/bin/env python

# Project Euler
# Problem 44
# http://projecteuler.net/problem=44

import math

def quadform(a,b,c):
    det = b**2.0-4.0*a*c
    if det>0:
        detsqrt = math.sqrt(det)
        return [(-b + detsqrt)/(2.0*a),(-b - detsqrt)/(2.0*a)]
    if det<0: return []
    if det==0: return [-b/(2.0*a)]

def ispent(n):
    roots = filter(lambda x: x>0 and int(x)==x, quadform(3,-1,-(n*2)))
    #print len(roots)
    return len(roots)==1


pentNums = [1]

i=2
#for i,j in enumerate(xrange(1,24)):
#    print i,j,ispent(j)

#while pentNums[len(pentNums)-1]:
for x in xrange(2,10):
    '''pentNums.append(i*(3*i-1)/2.0)
    for i in xrange(len(pentNums)):
        for j in xrange(i,len(pentNums)):
            # j>i
            print pentNums[i],pentNums[j]
            #print "Sum:",pentNums[j]+pentNums[i]
            #print "Diff:",pentNums[j]-pentNums[i]
            if pentNums[j]>pentNums[i] and ispent(pentNums[j]+pentNums[i]):
                print pentNums[i],pentNums[j]
                if ispent(pentNums[j]-pentNums[i]):
                    print pentNums[i],pentNums[j]'''

    pentNums.append(x*(3*x-1)/2.0)
    #print (x*(3*x-1)/2.0)
    for i in reversed(xrange(0)): # artifact of previous code
    #for i in reversed(xrange(len(pentNums))):
        for j in reversed(xrange(i,len(pentNums))):
            # j>i
            print pentNums[i],pentNums[j]
            #print "Sum:",pentNums[j]+pentNums[i]
            #print "Diff:",pentNums[j]-pentNums[i]
            if pentNums[j]>pentNums[i] and ispent(pentNums[j]+pentNums[i]):
                print pentNums[i],pentNums[j]
                if ispent(pentNums[j]-pentNums[i]):
                    print pentNums[i],pentNums[j]
i=9
#print pentNums
while(True):
    #if(i%100==0): print i
    pentNums.append(i*(3*i-1)/2.0)
    for j in reversed(xrange(0,len(pentNums))):
        # j>i
        #print i,j, len(pentNums)
        #print pentNums[i],pentNums[j]
        #print "Sum:",pentNums[j]+pentNums[i]
        #print "Diff:",pentNums[j]-pentNums[i]
        if pentNums[j]<pentNums[i] and ispent(pentNums[j]+pentNums[i]):
            #print pentNums[i],pentNums[j]
            if ispent(pentNums[i]-pentNums[j]):
                #print i,j,pentNums[i],pentNums[j],(pentNums[i]-pentNums[j])
                print int(pentNums[i]-pentNums[j])
                exit(0)
    i+=1
