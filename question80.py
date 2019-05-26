#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Square root digital expansion
#Problem 80 
#It is well known that if the square root of a natural number is not an integer, then it is irrational. The decimal expansion of such square roots is infinite without any repeating pattern at all.

#The square root of two is 1.41421356237309504880..., and the digital sum of the first one hundred decimal digits is 475.

#For the first one hundred natural numbers, find the total of the digital sums of the first one hundred decimal digits for all the irrational square roots.



#idea - make list of all squares, then find find decimal sums of others


import time
from decimal import *
import math
getcontext().prec = 102

s1=time.time()


squares = [i*i for i in range(2,101)]
#print(squares)

res = 0.0
for j in range(2,101):
	if j not in squares:
		#print(j)
		temp = Decimal(j).sqrt()
		temp2 = math.floor(temp)
		
		temp = Decimal(temp) - temp2
		#print(str(temp)[90:102])
		#print(len(str(Decimal(temp))[2:102]))
		res+= sum([int(char) for char in str(temp)[2:101]])
		res+= temp2	


print(res)

		



print("{}s".format(time.time() - s1))

# 40886.0 YAY
# 0.002087831497192383s


