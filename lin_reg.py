x = [69, 63, 66, 64, 67, 64, 70, 66, 68, 67, 65, 71]
y = [70, 65, 68, 65, 69, 66, 68, 65, 71, 67, 64, 72]

n = len(x)
s_x = sum(x)
s_y = sum(y)
s_x2 = sum(i*i for i in x)
s_xy = sum(x*y for x,y in zip(x,y))

#This is very inefficient and unpythonic
# sum = 0
# for index_x,value_x in enumerate(x):
# 	for index_y,value_y in enumerate(y):
# 		if index_y==index_x:
# 			sum += value_x*value_y
# s_xy = sum

a = (n*s_xy - s_x*s_y)/(n*s_x2-(s_x*s_x))
b = (s_y - a*s_x)/n

print("a: ",a)
print("b: ",b)

print("Required best fitted line: y = ",a,"x + ",b)