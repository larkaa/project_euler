#!/usr/bin/env python3

# Sub-string divisibility
#Problem 43
#The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

#Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

#d2d3d4=406 is divisible by 2
#d3d4d5=063 is divisible by 3
#d4d5d6=635 is divisible by 5
#d5d6d7=357 is divisible by 7
#d6d7d8=572 is divisible by 11
#d7d8d9=728 is divisible by 13
#d8d9d10=289 is divisible by 17
#Find the sum of all 0 to 9 pandigital numbers with this property.

import time
start_time = time.time()

import itertools

result = []

for pan_iter in list(itertools.permutations('0123456789')):

  if pan_iter[0]!=0:
    #num = int(''.join(map(str,pan_iter)))
    if int(''.join(str(pan_iter[1])+str(pan_iter[2])+str(pan_iter[3]))) %2==0:
     if int(''.join(str(pan_iter[2])+str(pan_iter[3])+str(pan_iter[4]))) %3==0:
      if int(''.join(str(pan_iter[3])+str(pan_iter[4])+str(pan_iter[5]))) %5==0:
       if int(''.join(str(pan_iter[4])+str(pan_iter[5])+str(pan_iter[6]))) %7==0:
        if int(''.join(str(pan_iter[5])+str(pan_iter[6])+str(pan_iter[7]))) %11==0:
         if int(''.join(str(pan_iter[6])+str(pan_iter[7])+str(pan_iter[8]))) %13==0:
          if int(''.join(str(pan_iter[7])+str(pan_iter[8])+str(pan_iter[9]))) %17==0:
            result.append(int(''.join(map(str,pan_iter))))

print(sum(result))




print ('--- %s seconds ---' % (time.time()-start_time))

# 16695334890 YAY
# 8 seconds


