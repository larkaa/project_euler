#!/usr/bin/env python3

# question 37

#The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

#Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

#NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.


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

def truncate(num,list_primes):
  num_str=str(num)
  #print(num_str)
  a=1
  for i in range(1,len(num_str)):
    check_str = num_str[0:-i]
    check = int(check_str)
    #print(' ',check)
    if check not in list_primes:
      a=0
      return 0
  if a==1:
    for i in range(1,len(num_str)):
      check_str = num_str[i:]
      check = int(check_str)
      #print(' ',check)
      if check not in list_primes:
        a=0
        return 0
  return 1




#print(truncate(12345))


def find_trunc_primes(limit):
  primes = find_primes(limit)
  #primes = [3797,11,3,7,379,]
  res = []
  for prime in primes:
    if prime <10:
      temp=0
    else:
      # check if it can be truncated one way
      check1 = truncate(prime,primes) 
      # then check the reverse
      #temp = str(prime)
      if check1==1:
        res.append(prime)
  return res

#print(find_trunc_primes(10000))
final = find_trunc_primes(1000000)
print(final)
print(sum(final))

# [23, 37, 53, 73, 313, 317, 373, 797, 3137, 3797, 739397]
# 748317 YAY








