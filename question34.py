#!/usr/bin/env python3

# quesiton 34 digit factorials

#145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

#Find the sum of all numbers which are equal to the sum of the factorial of their digits.

#Note: as 1! = 1 and 2! = 2 are not sums they are not included.

#idea brute force
# note that 
# 3 != 3!, similar up to 11, 12, 13, and 14 up is too high. start with 20 
# 14 = 1 + 24 NOPE
# 15 = 1 + too high

def factorial(num):
  if num==0: return 1
  if num==1: return 1
  else:
    res=num
    num-=1
    while num>1:
      res *= num
      num-=1

  return(res)

# to speed things up pre-calculate the factorials
# to be used in the following function
fact_list =[]
for i in range(10):
  fact_list.append(factorial(i))


def digit_factorial(num):
  num_str = str(num)
  temp_sum = 0
  for char in num_str:
    temp_sum+= fact_list[int(char)]
  return temp_sum


def find_numbers(limit):
  res_list = []
  for i in range(3,limit+1):
    temp = digit_factorial(i)
    if i == temp:
      res_list.append(i)
  return res_list


#print(digit_factorial(1546))
# 145 is the smallest!
# note that 9! = 362880, 7*9 < 9999999

print(find_numbers(1000000))
# there are only two!
# [145, 40585]
# sum = 40730

