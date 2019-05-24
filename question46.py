#!/usr/bin/env python3



# Goldbach's other conjecture
#Problem 46
#It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

#9 = 7 + 2×12
#15 = 7 + 2×22
#21 = 3 + 2×32
#25 = 7 + 2×32
#27 = 19 + 2×22
#33 = 31 + 2×12

#It turns out that the conjecture was false.

#What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

import time
start_time = time.time()


def return_primes(num):
  candidate_nums = [x for x in range(num)]
  # indexes are the numbers themselves
  for i in range(2,num):
    if candidate_nums[i]:
      #sum_res += i
      #print(i,sum)
      for j in range(i*i,num,i):
        candidate_nums[j] = 0
  res = [y for y in candidate_nums if y>1]
  #comp_odd = [i for i, x in enumerate(candidate_nums) if x==0]
  return(res,comp_odd)

limit = 100000
primes = return_primes(limit)
#squares=[ i*i for i in range(1,int(limit**.5))]

a=True
i=33
# format i = p + 2×square, (i-p)/2 == square
while a:
  if i>limit: a=False; print("fail")
  elif i in primes: i+=2
  else:
    p_temp = [y for y in primes if y<i]
    count = 0
    for p in p_temp:
      temp = (i - p)/2
      #if temp in squares: count+=1
      if temp**.5==int(temp**.5): count+=1
    if count==0: 
      print(i); a=False
    i+=2

# 5777 YAY
# 72 seconds if comparing a list of squares
# 19 seconds if checking square roots

#print(primes)
#print(squares)


print ('--- %s seconds ---' % (time.time()-start_time))

