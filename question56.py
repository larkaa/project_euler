#!/usr/bin/env python3

# Powerful digit sum
#Problem 56
#A googol (10^100) is a massive number: one followed by one-hundred zeros; 100100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

#Considering natural numbers of the form, a^b, where a, b < 100, what is the maximum digital sum?

import time
start_time = time.time()


def power(a,b):
  if b==0: return 1
  elif b==1: return a
  else:
    temp = a
    for i in range(b-1):
      temp *= a
  return temp

	

def sum_digits(n):
   r = 0
   while n:
       r, n = r + n % 10, n // 10
   return r

limit = 100

count=0
resa = 0
resb = 0
for a in reversed(range(1,101)):
  for b in reversed(range(1,101)):
    temp = sum_digits(power(a,b))
    if temp>count:
      count = temp
      resa = a
      resb = b
      print(" ",a,"^",b)
print(count,resa,resb)

#972 = 99 ^95
#--- 0.25336360931396484 seconds ---


print ('--- %s seconds ---' % (time.time()-start_time))

#  4075 YAY
# --- 0.035889387130737305 seconds ---

