#!/usr/bin/env python3

# Pandigital multiples
#Problem 38
#Take the number 192 and multiply it by each of 1, 2, and 3:

#192 × 1 = 192
#192 × 2 = 384
#192 × 3 = 576
#By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

#The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

#What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?

import time
start_time = time.time()


# n>1, so if n=2, then y must be max 5 digits long 
# max n is 9, so y can be 1 digit long


result=[(192,3,192384576),(9,5,918273645)] 
# (y,n,digit) given in examples


for y in range(1,10000):
  digits = ''
  n=1
  while len(digits)<9:
    digits = digits+ str(n*y)
    if len(digits)==9:
      if "".join(sorted(digits))=='123456789':
        result.append((y,n,int(digits)))
    n+=1


#print(result)
def getKey(item):
  return item[2]

print(sorted(result, key=getKey))

print ('--- %s seconds ---' % (time.time()-start_time))
# 0.03 seconds

# [(1, 9, 123456789), (192, 3, 192384576), (192, 3, 192384576), (219, 3, 219438657), (273, 3, 273546819), (327, 3, 327654981), (6729, 2, 672913458), (6792, 2, 679213584), (6927, 2, 692713854), (7269, 2, 726914538), (7293, 2, 729314586), (7329, 2, 732914658), (7692, 2, 769215384), (7923, 2, 792315846), (7932, 2, 793215864), (9, 5, 918273645), (9, 5, 918273645), (9267, 2, 926718534), (9273, 2, 927318546), (9327, 2, 932718654)]

# YAY




def is_pan(num_str):
  numbers = list(range(1,len(num_str)+1))
  for i in range(0,len(num_str)):
    if int(num_str[i]) in numbers:
      ind = numbers.index(int(num_str[i]))
      del numbers[ind]
  if len(numbers)==0: return 1
  else: return 0
  return 0

