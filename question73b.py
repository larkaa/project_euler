#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Counting fractions in a range
# Problem 73 
# Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

# If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

# 1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

# It can be seen that there are 3 fractions between 1/3 and 1/2.

# How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper fractions for d ≤ 12,000?

# 1. check each divisor, then loop between 1/3 and 1/2 of this value, add to list
# 2. check value against saved list to not double count


import time
import math
from fractions import gcd
s1=time.time()

count=0

def count_middle(limit):
	res = []
	lower = 1.0/3
	upper = 0.5

	for den in range(2,limit+1):
		d_lower = int(math.ceil(den/3))
		d_upper = int(math.ceil(den*0.5))

		

		for num in range(d_lower,d_upper):
			if gcd(den,num)==1:
				res.append(den/(1.0*num))
				#print(den,num)
	#print(res)
	
	return(len(res)-1)
	
test = count_middle(12000)
print()
print(test)
			

print("{}s".format(time.time() - s1))

# 7295372
#16.801006078720093s
