#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Counting summations
# Problem 76 
# It is possible to write five as a sum in exactly six different ways:

# 4 + 1
# 3 + 2
# 3 + 1 + 1
# 2 + 2 + 1
# 2 + 1 + 1 + 1
# 1 + 1 + 1 + 1 + 1

# How many different ways can one hundred be written as a sum of at least two positive integers?

# idea, 
# 1xn
# 2 -> 1+1... 3-> 2+1, 1+1+1
#4 -> 1+1.., 2+1+1, 2+2, 3+1

# [2/1, 3/2, 4/3, 5/6] 
import time
s1=time.time()

# this one takes too long
def partition(k,n):
	res = 0
	if k>n: 
		return(0)
		
	if k==n: 
		return(1)
		
	
	res = partition(k+1,n) + partition(k,n-k)
	return(res)
	

#using a generating function
def partition2(k,n):

	for i in range(2,n):
		temp = 0
		for j in range(1,i):
			temp+=(-1)**(j+1)*(p[n-0.5*j*(3*j01)]+p[n-0.5*j*(3*j+1)])
		p[i] = temp
	return(p[-1])


# trial one by iteration is too long
print(partition(1,100)-1)
# 190569291
# 271.16158080101013s


# trail two by generating function is...
p = [0 for i in range(n+1)]
p[0]=1
p[1]=1
print(partition2(1,100)-1)



print("{}s".format(time.time() - s1))


