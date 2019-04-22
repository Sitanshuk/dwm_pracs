#kmeans algorithms for k=2

from math import sqrt
x = [1,1.5,3,5,3.5,4.5,3.5]
y = [1,2,4,7,5,5,4.5]
points = list(zip(x,y))
def dist(p1,p2):
	x,y = p1
	x1,y1 = p2
	return sqrt((y-y1)**2+(x-x1)**2)

c1 = points[0]
c2 = points[-1]
temp1 = list()
temp2 = list()
while True:
	k1 = list()
	k2 = list()
	#adding points to a cluster
	for p in points:
		if dist(c1,p) < dist(c2,p):
			k1.append(p)
		else:
			k2.append(p)

	#calculating centroids of each cluster
	try:
		c1 = (sum(x for x,y in k1)/len(k1),sum(y for x,y in k1)/len(k1))
		c2 = (sum(x for x,y in k2)/len(k2),sum(y for x,y in k2)/len(k2))
	except:
		pass
	if k1==temp1 and k2==temp2:
		break
	temp1 = k1[:]
	temp2 = k2[:]
print("k1: ",k1)
print("k2: ",k2)
