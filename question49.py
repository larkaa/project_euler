#!/usr/bin/env python3

#Prime permutations
#Problem 49
#The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

#There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

#What 12-digit number do you form by concatenating the three terms in this sequence?


# idea - in steps
# 1, keep only 4 digit primes. how many are there? 1061!
# 2, 


# find prime with limit num
## sieve of eratosthenes
# modified to keep only 4 digit primes
def find_primes():
  num = 10000
  candidate_nums = [x for x in range(num)]
  # indexes are the numbers themselves
  for i in range(2,num):
    if candidate_nums[i]:
      #sum_res += i
      #print(i,sum)
      for j in range(i*i,num,i):
        candidate_nums[j] = 0
  res = [y for y in candidate_nums if y>999]
  return(res)

primes = find_primes()

# count permutations for each prime
def is_permutation(num1,num2):
  num1_str = str(num1)
  num2_str = str(num2)

  for char in num1_str:
    if char not in num2_str: return 0
  for char in num2_str:
    if char not in num1_str: return 0
  return 1

def return_permutations(num, num_list):
  res = [num]
  for check in num_list:
    if num==check:
      temp = 0
    else: 
      if is_permutation(num,check):
        res.append(check)
  return res

def count_permutations():
  length = len(primes)
  counts = [0]*length
  res_sum = 0

  # first count permutations
  for i in range(length):
    if counts[i]==0:
      for j in range(i,length):
        res_sum = is_permutation(primes[i],primes[j])
        counts[i] += res_sum
        counts[j] += res_sum
        #if res_sum>0: counts[i].append(primes[i])

  # go back and check only those with counts>=3
  candidates = [primes[y] for y in range(len(counts)) if counts[y]>=3] 

  # get permutation list
  for a in candidates:
    perm_list = return_permutations(a,candidates)
    

# now choose only those that have 3+ permutations in the primes
temp = count_permutations()
print(temp)

#candidates = [primes[y] for y in range(len(temp)) if temp[y]>=3]

#def get


#for i in range(10):
#  temp1 = sum([1 for y in temp if y==i])
#  print(temp1,' have count == ', i)
# print(primes[0])
# print(len(primes))
# 1009
# 1061








