#!/usr/bin/env python3

# Permuted multiples
#Problem 52
#It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

#Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

import time
start_time = time.time()

a=True
i=10
while a:
  i_str = str(i)
  compare = "".join(sorted(i_str))
  t1 = 6*i
  if "".join(sorted(str(t1)))==compare:
    t1 = 5*i
    if "".join(sorted(str(t1)))==compare:
      t1 = 4*i
      if "".join(sorted(str(t1)))==compare:
        t1 = 3*i
        if "".join(sorted(str(t1)))==compare:
          t1 = 2*i
          if "".join(sorted(str(t1)))==compare:
            print(i)
            a=False
  i+=1


print ('--- %s seconds ---' % (time.time()-start_time))

# 142857 YAY
# 0.38 sec


