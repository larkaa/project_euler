#!/usr/bin/env python3

# Combinatoric selections
#Problem 53
#There are exactly ten ways of selecting three from five, 12345:

#123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

#In combinatorics, we use the notation, 5C3 = 10.

#In general,

#nCr =	
# n! / r!(n−r)!
#,where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.
#It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

#How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ 100, are greater than one-million?

import time
start_time = time.time()


limit = 100

def nCk(n,k):
  res = 1
  for i in range(1,k+1):
    res *=(n+1-i)/i
  return res

# note that when r=0 or r=n, then solution is 1

count=0
for n in range(23,101):
  for k in range(2,n):
    if nCk(n,k)>1000000:
      count+=1
print(count)

print ('--- %s seconds ---' % (time.time()-start_time))

#  4075 YAY
# --- 0.035889387130737305 seconds ---

