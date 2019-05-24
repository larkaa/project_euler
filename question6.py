#!/usr/bin/python

## question 6 euler
### answer
# this is the product of the square of sum minus the individual squared terms

# multinomial thereom: will be of from
# a^2 + ... + c^2 + 2ab + 2ac +...

def diff_sum_squares(num):
  i = 0
  j = 0
  sum = 0
  for i in xrange(1,num+1):
    for j in xrange(1,i):
      sum = sum + 2*i*j
  return(sum)


test = diff_sum_squares(10) # true answer is 3025-285 = 2640
print (test)
test = diff_sum_squares(100)
print (test) # 25164150
