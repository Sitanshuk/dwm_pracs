webworld = [[0,1,1,0],
			[0,0,0,1],
			[1,1,0,1],
			[0,0,1,0],
			]
pr = list()
for page in webworld:
	pr.append(1/len(page))
print(pr)
count = 0
while count < 3:
	temp = list()
	for x in range(len(pr)):
		s = 0.0
		for i,page in enumerate(webworld):
			if page[x] == 1: #add only if it is incoming edge
				s += pr[i]/sum(page)
		temp.append(s)	#to ensure that pagerank in formula is from previous iteration only
	pr = temp
	print(pr)
	print(sum(pr)) 
	count += 1