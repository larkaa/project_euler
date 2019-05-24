#!/usr/bin/python
# -*- coding: utf-8 -*-


#Diophantine equation
#Problem 66
#Consider quadratic Diophantine equations of the form:

#x2 – Dy2 = 1

#For example, when D=13, the minimal solution in x is 649 2 – 13×180 2 = 1.

#It can be assumed that there are no solutions in positive integers when D is square.

#By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:

#3^2 – 2×2^2 = 1
#2^2 – 3×1^2 = 1
###9^2 – 5×4^2 = 1
#5^2 – 6×2^2 = 1
#8^2 – 7×3^2 = 1

#Hence, by considering minimal solutions in x for D ≤ 7, the largest x is obtained when D=5.

#Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained.

import time
import gmpy 
import gmpy2

start_time = time.time()

# brute force too slow
# try listing all squares, then reverse calculate answer
# NOPE

# This is pell's equation, and the solution involved is
# the chakravala method


#x*x - D*y*y = 1
#x = sqrt(1+D*y*y)

from fractions import Fraction
def solvePellsEqn(D):
	'''
	 solve the equation, x**2-D*y**2=1, where D, x,y are integers
	 reference: chakravala method
	'''
	def firstGuess():
		#first guess y=1
		x = 0 #y=1
		while x ** 2 < D:x += 1
		k = x * x - D
		k1 = (x - 1) * (x - 1) - D
		if -k1 < k: return (x - 1, 1, k1)
		else: return (x, 1, k)
	def chakravala(x, y, k):
		# chakravala step
		# scaling down by kp after composing the solution
		# (x,y,k) with (m,1,m**2-D) gives
		# ( (x*m+D*y)/|k| , (x+y*m)/|k| , (m**2-D)/k )
		# find an integer m s.t., k divides (x+y*m) and abs(m**2-D) is minimal
		# 	 	1. find r s.t., m=k*t+r, which makes (x+y*m) divisible by k
		#		2. find t, which minimizes abs(m**2-D)
		r = 0
		while (x + y * r) % k != 0: r += 1
		m = r
		while m ** 2 < D: m += abs(k)
		m1 = m - abs(k)
		if m1 > 0 and abs(m1 ** 2 - D) < abs(m ** 2 - D):
			m = m1
		return ((x * m + D * y) / abs(k) , (x + y * m) / abs(k) , (m ** 2 - D) / k)
	def compose(x1, y1, k1, x2, y2, k2):
		xr, yr, kr = x1 * x2 + D * y1 * y2 , x1 * y2 + x2 * y1 , k1 * k2
		if kr in (-4, 4):
			xr /= 2
			yr /= 2
			kr /= 4
		return (xr, yr, kr)
	
	(x, y, k) = firstGuess()
	x, y = Fraction(x, 1), Fraction(y, 1)
	while k not in (1, 2, 4, -1, -2, -4):
		(x, y, k) = chakravala(x, y, k)
	if k in (4, -4):
		x /= 2
		y /= 2
		k /= 4
	x1, y1, k1 = x, y, k
	while x.denominator != 1 or k != 1:
		(x, y, k) = compose(x, y, k, x1, y1, k1)
	return int(x), int(y)
	
maxD = 1000
res = []
for D in xrange(2, maxD + 1):
	if int(D ** 0.5) ** 2 == D: continue
	res.append((solvePellsEqn(D), D))
print max(res)

# 661 YAY
# ((x = 16421658242965910275055840472270471049L, 
#   y = 638728478116949861246791167518480580L), 661)


print ('  %s seconds ---' % (time.time()-start_time))



