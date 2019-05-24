#!/usr/bin/env python3

#question 23 non-abundant sums

# a perfect number is equal to the sum of it's proper divisors
# 28 = 1+2+4+7+14

# n is deficient if the sum of it's proper divisors is less than n
# n '' abundant if the sum is greater than n

# 12 is the smallest abundant number
# 24 is the smallest sum of 2 ab numbers

# analysis shows that all int > 28123  can be 
# written as the sum of two abundant numbers, although we know that
# But we know that the greatest number that cannot be written by
# a sum of 2 ab numbers is less than this

# find the sum of all positive integers which cannot
# be written as the sum of two abundant numbers


# idea
# brute force analysis
# skip multipliers of 2 for odd numbers


# idea: first find all abundant numbers
# then find all possible 2-sums of these numbers
# print out those that are not included

# funciton fo find abundant sums
def find_abundant(limit):
  number_vector = list(range(limit+1)) # result vector
  #print(number_vector)
  #type(number_vector)
  for num in number_vector:
    temp = sum_divisors(num)
    if temp<=num: 
      number_vector[num]=0
  return([y for y in number_vector if y>0])

def sum_divisors(number):
  if number==0: return 0
  elif number==1: return 1
  else:
    temp_sum = 0
    i=1
    while (i<number//2+1):
      if number%i==0:
        #print(number, i)
        temp_sum+=i
      if number%2!=0: i+=2
      else: i+=1
  return temp_sum

# function to find sums of all abundant numbers
def find_sums_abundant(limit):
  abun_list = find_abundant(limit)
  #print(abun_list)
  res_list = list(range(limit+1))
  for i in abun_list:
    for j in abun_list:
      if i+j <= limit:
        res_list[i+j] = 0
  return([y for y in res_list if y>0])



# largest possible is = 28123, given in problem

res = find_sums_abundant(28123)
print(sum(res))
# 4179871 YAY


