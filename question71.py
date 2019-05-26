#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Ordered fractions
#Problem 71 
#Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

#If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

#1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

#It can be seen that 2/5 is the fraction immediately to the left of 3/7.

#By listing the set of reduced proper fractions for d ≤ 1,000,000 in ascending order of size, find the numerator of the fraction immediately to the left of 3/7.


import time
import math
import fractions
from fractions import gcd
s1=time.time()





def find_frac(limit):
	lower = 2.0/5
	upper = 3.0/7
	#limit = 8
	res= 2
	for den in range(limit,1,-1):
		#print(den)
		nlower = math.floor(lower*den)
		nupper = math.ceil(upper*den)
		for num in range(nlower,nupper):
			if gcd(num,den)==1:
				if num/(1.0*den)<upper:
					#print(num,den,num/den)
					if num/(1.0*den)>lower:
						lower = num/(1.0*den)
						res = num
	return(res)

	
#test = count_fracs2(8)
#test = count_fracs2(1000000)

print(find_frac(1000000))
#print(test)
print("{}s".format(time.time() - s1))

# 428570
#2.031975269317627s

