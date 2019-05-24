#!/usr/bin/env python3

# quesiton 32 pandigital products

#We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

#The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

#Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

#HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

# idea this is like setting up the right side and choosing all combinations of products

# (one digits) * (three to four digits) = (four digits)

def is_pandigital(num):
  num_str = str(num)
  numbers = list(range(1,len(num_str)+1))
  for i in range(0,len(num_str)):
    if int(num_str[i]) in numbers:
      ind = numbers.index(int(num_str[i]))
      del numbers[ind]
  if len(numbers)==0: return 1
  else: return 0
  return 0

print(is_pandigital(12345))
