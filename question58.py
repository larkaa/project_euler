#!/usr/bin/env python3

# Spiral primes
#Problem 58
#Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

# 37 36 35 34 33 32 31
# 38 17 16 15 14 13 30
# 39 18  5  4  3 12 29
# 40 19  6  1  2 11 28
# 41 20  7  8  9 10 27
# 42 21 22 23 24 25 26
# 43 44 45 46 47 48 49

#It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

#If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?

# idea
# only calculate the diagonals
# store the length and the number of primes
# stop when ratio < .1
import time
start_time = time.time()

# more efficient storage
# using numpy matrices

import numpy
def find_primes(limit):
    is_prime = numpy.ones(limit, dtype=numpy.bool)
    for n in range(2, int(limit**0.5 + 1.5)): 
        if is_prime[n]:
            is_prime[n*n::n] = 0
    return numpy.nonzero(is_prime)[0][2:]

def find_largest(primes):
  compare = '123456789'
  for p in reversed(primes):
    p_str = str(p)
    p_len = len(p_str)
    if "".join(sorted(p_str))==compare[0:p_len]:
      return p
  return 0


# note formula for the square is
# (2n-1)^2 ... -n, -2n, -3n for the other vertices


n=2
count_p = 0
count = 1
ratio=1
limit =  10000000
primes = find_primes(limit)
#print(primes)
v1=0
while ratio >=0.1 and v1<primes[-1]:
  v1 = (2*n-1)*(2*n-1)
  v2 = v1 - n
  v3 = v2 - n
  v4 = v3 - n

  print("size: ",2*n-1, "n=",n, "count=",count)
  print(v1,v2,v3,v4)
  if n==0: count=1
  if v1 in primes:
    count_p +=1
  if v2 in primes:
    count_p +=1
  if v3 in primes:
    count_p +=1
  if v4 in primes:
    count_p +=1
  count +=4
  
  if count>10:
    ratio = count_p/count
  if ratio<0.1:
    print("Done at: ",2*n-1)
  if v1>primes[-1]: 
    ratio = count_p/count
    print("end of primes")
    print("Ratio: ",ratio,"Primes :", primes[-1], "End: ",v1)
    ratio = 0.001
  n+=1  
    


print(ratio,2*(n-1)-1) #,count,count_p,primes[-1])
print ('  %s seconds ---' % (time.time()-start_time))

#  1911 ???
    
