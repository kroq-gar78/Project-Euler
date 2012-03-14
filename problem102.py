#!/usr/bin/env python

# Project Euler
# Problem 102
# http://projecteuler.net/problem=102

# Using triangles.txt [renamed to 'problem102_dat.txt'], a 27K text file
# containing the co-ordinates of one thousand "random" triangles, find
# the number of triangles for which the interior contains the origin.

def triContains(triangle,point):
	x,y=point
	#lines=getLines(triangle)
	lines=getSigns(triangle)
	contains=True
	for i in lines:
		if(i[3]=='>'):
			#if(y<i[0]*x+i[1]):
			if(x*i[0]+y*i[1]<i[2]):
				contains=False
				break
		else:
			if(x*i[0]+y*i[1]>i[2]):
				contains=False
				break
	return contains

def getSigns(triangle):
	x,y=getCentroid(triangle)
	lines=getLines(triangle)
	for i in xrange(len(lines)):
		#if(y>=lines[i][0]*x+lines[i][1]): lines[i][2]='>'
		if(x*lines[i][0]+y*lines[i][1]>lines[i][2]): lines[i][3]='>'
		else: lines[i][3]='<'
	return lines

def getCentroid(triangle):
	x=[0,0,0]
	y=[0,0,0]
	centroid=[0,0]
	for i in xrange(len(triangle)):
		x[i],y[i]=triangle[i]
		centroid[0]+=x[i]
		centroid[1]+=y[i]
	centroid[0]=centroid[0]/3
	centroid[1]=centroid[1]/3
	return centroid[0],centroid[1]
	
def getLines(triangle):
	lines = []
	for i in xrange(len(triangle)):
		#print triangle[i],triangle[(i+1)%(len(triangle))]
		lines.append(ptslope(triangle[i],triangle[(i+1)%(len(triangle))]))
	return lines

# for ptslope(),
# using form 'ax+by=c'
# ret[0]=a,ret[1]=b,ret[2]=c
# ret[3]=sign (>=, <=, =)
def ptslope(pt1,pt2):
	x = [0,0]
	y = [0,0]
	x[0],y[0] = pt1
	x[1],y[1] = pt2
	
	if(x[0]-x[1]==0): return [1,0,x[0],'=']
	slope = (y[0]-y[1])/(x[0]-x[1])
	if(slope==0): return [0,1,y[0],'=']
	
	# (y-y[0])/(x-x[0])=slope
	# y = slope(x-x[0])+y[0]
	# y = slope(x) - slope*x[0] + y[0]
	# y-int = -slope*x[0] + y[0]
	# slope = (y-y[0])/(x-x[0])
	
	#line = [slope,-(slope*x[0])+y[0],'=']
	
	# ax+by=c
	# y = slope*x - slope*x[0] + y[0]
	# y - slope*x = -slope*x[0] + y[0]
	# (y/slope-x) = (-slope*x[0]+y[0])/slope
	# y/slope - x = -x[0]+y[0]/slope
	# -x + y/slope = -x[0]+y[0]/slope
	# [-1,slope,(-x[0]+y[0]/slope)]
	
	return [-1,1/slope,(-x[0]+y[0])/slope,'=']
	

f = open('problem102_data.txt','r')
triangles = f.readlines()
for i in xrange(len(triangles)):
	oldpoints = triangles[i].split(',')
	points = []
	#points[0] = oldpoints[0],oldpoints[1]
	for j in xrange(3):
		points.append((float(oldpoints[j*2].strip('\n\r')),float(oldpoints[j*2+1].strip('\n\r'))))
	triangles[i] = points
	#print points
print(len(triangles))
answer = 0
for i in triangles:
	if( triContains(i,(0,0)) ): answer+=1
	print triContains(i, (0,0))
print answer
	
#print triangles[0]
#print triContains(triangles[0],(0,0)),triContains(triangles[1],(0,0))
#print ptslope((0,1),(1,0))
#print getLines(triangles[0])
