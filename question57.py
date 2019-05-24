#!/usr/bin/env python3

# Square root convergents
#Problem 57
#It is possible to show that the square root of two can be expressed as an infinite continued fraction.

#√ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

#By expanding this for the first four iterations, we get:

#1 + 1/2 = 3/2 = 1.5
#1 + 1/(2 + 1/2) = 7/5 = 1.4
#1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
#1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

#The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 1393/985, is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.

#In the first one-thousand expansions, how many fractions contain a numerator with more digits than denominator?


# note:
# sequence is 1, 3/2, 7/5,...
# p/q, p+2q/(p+q)

import time
start_time = time.time()


p=1
q=1
count = 0

for i in range(1,1001):
  num = p+2*q
  den = p+q

  if len(str(num))>len(str(den)):
    count+=1

  p = num
  q = den

print(count)
print (' %s seconds ---' % (time.time()-start_time))



#  153 YAY
# --- 0.0065348148345947266 seconds 

