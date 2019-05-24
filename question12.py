#!/usr/bin/env python3

#question 12: triangle numbers (1+2+3+4=10)

# 28: 1,2,4,7,14,28
# We can see that 28 is the first triangle number to have over five 
# divisors.

# What is the value of the first triangle number to have over five 
# hundred divisors?


## answer : count the exponents in the prime factorization


def find_prime_factors(num):
  i=2
  prime_factors = []
  while (i*i<num):
    while(num%i==0):
      prime_factors.append(i)
      num /= i
    i=i+1
  if (num != 1): prime_factors.append(int(num))
  return(prime_factors)


def num_factors(num):
  primes = find_prime_factors(num)
  unique_primes = set(primes)
  total_factors = 1
  for j in unique_primes:
    total_factors *= primes.count(j)+1
  return(total_factors)

def triangle_number(index):
  if index==1: return 1
  triangle = 0
  for i in range(1,index+1):
    triangle += i
  return triangle

def largest_triangle_divisors(limit):
  a=1
  i=0
  while a:
    i=i+1
    tri_num = triangle_number(i)
    temp = num_factors(tri_num)
    if(temp>limit):
      print(tri_num)
      a=0
      return(tri_num)
  return(0)

temp= (largest_triangle_divisors(500))
print(find_prime_factors(temp))
#print(triangle_number(1),triangle_number(2),triangle_number(4))

# answer 76576500
# prime factors [2, 2, 3, 3, 4, 4, 4, 7, 11, 13, 17]


