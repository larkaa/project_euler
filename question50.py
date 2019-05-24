#!/usr/bin/env python3



# Consecutive prime sum
# Problem 50
#The prime 41, can be written as the sum of six consecutive primes:

#41 = 2 + 3 + 5 + 7 + 11 + 13
#This is the longest sum of consecutive primes that adds to a prime below one-hundred.

#The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

#Which prime, below one-million, can be written as the sum of the most consecutive primes?


def return_primes(num):
  
  candidate_nums = [x for x in range(num)]
  # indexes are the numbers themselves
  for i in range(2,num):
    if candidate_nums[i]:
      #sum_res += i
      #print(i,sum)
      for j in range(i*i,num,i):
        candidate_nums[j] = 0
  res = [y for y in candidate_nums if y>1]
  return(res)

primes = find_primes(1000000)

# find longest sum where the 

