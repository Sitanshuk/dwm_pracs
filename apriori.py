trans = [['I1','I2','I5'],
		['I2','I4'],
		['I2','I3'],
		['I1','I2','I4'],
		['I1','I3'],
		['I2','I3'],
		['I1','I3'],
		['I1','I2','I3','I5'],
		['I1','I2','I3']]
s_count = 2
confidence = 75
count_item = {}
#iteration 1
#makes a dictionary that counts accurance of each item
for t in trans:
	for x in t: 
		if x in count_item.keys():
			count_item[x] += 1
		else:
			count_item[x] = 1
d = []
#deletes Items count < support
for k,v in count_item.items():
	if v<s_count:
		d.append(k)
for k in d:
	del(count_item[k])
print(count_item)

#2nd iteration
count_2 = list()
item_2 = list()
for item1 in count_item.keys():
	for item2 in count_item.keys():
		if item1 != item2:
			item_2.append([item1,item2])
			count_2.append(0)
for i,item in enumerate(item_2):
	for x in trans:
		if all(j for j in item if j in x):
			count_2[i] +=1


print(item_2)
print(count_2)


