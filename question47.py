#!/usr/bin/env python3

# Distinct primes factors
#Problem 47
#The first two consecutive numbers to have two distinct prime factors are:

#14 = 2 × 7
#15 = 3 × 5

#The first three consecutive numbers to have three distinct prime factors are:

#644 = 2² × 7 × 23
#645 = 3 × 5 × 43
#646 = 2 × 17 × 19.

#Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?





# find prime with limit num
## sieve of eratosthenes
def find_primes(num):
  candidate_nums = [x for x in range(num)]
  # indexes are the numbers themselves
  for i in range(2,num):
    if candidate_nums[i]:
      #sum_res += i
      #print(i,sum)
      for j in range(i*i,num,i):
        candidate_nums[j] = 0
  res = [y for y in candidate_nums if y > 1]
  return(res)


#method 1
def num_prime_factors(n):
    factors = []
    num = n
    i = 2
    while i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            #print(i)
            factors.append(i)
    fact_set = set(factors)
    return(len(fact_set))
i=100000
a=True
while a:
  if num_prime_factors(i+3)==4:
    if num_prime_factors(i+2)==4:
      if num_prime_factors(i+1)==4:
        if num_prime_factors(i)==4:
          print(i,i+1,i+2,i+3)
          a=False
        else: i+=1
      else: i+=2
    else: i+=3
  else: i+=4

# 134043 134044 134045 134046
# YAY


#prime_list = find_primes(1000)

#temp = num_prime_factors(1308)
#print(temp)










