#!/usr/bin/env python3

# quesiton 35: circular primes
#The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

#There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

#How many circular primes are there below one million?

import itertools



## sieve of eratosthenes
def list_primes(num):
  candidate_nums = [x for x in range(num)]
  #upper_lim = int(num**(.5))
  # indexes are the numbers themselves
  for i in range(2,num):
    if candidate_nums[i]:
      #sum_res += i
      #print(i,sum)
      for j in range(i*i,num,i):
        candidate_nums[j] = 0
  res = [y for y in candidate_nums if y != 0]
  #print('791',candidate_nums[791])
  return(res)

#primes = list_primes(1000000)
#print(primes[1:150])

def circulate(num):
  num_str = str(num)
  new_str = ''
  for i in range(len(num_str)-1):
    new_str += num_str[i+1]
  new_str += num_str[0]
  return(int(new_str))

def find_circular_primes(limit):
  final_list = []
  primes = list_primes(limit)
  num_circ = 0
  for num in primes:
    a=0
    if num==1: a=1
    elif num<=11:
      final_list.append(num)
    else:
      #check for 2s or 5s
      check = str(num)
      for char in check:
        if int(char)%2==0:
          a=1; break
        if int(char)%5==0:
          a=1; break
      #print(num,a)
      if a==0:
        num_circ = num
        for j in range(len(str(num))-1):
          num_circ = circulate(num_circ)
          #print('  ',num_circ,a)
          if num_circ not in primes:
            a=1;
            break;
      #print('    ',a)
      if a==0: final_list.append(num)
  return(final_list)

final_list = find_circular_primes(1000000)
print(final_list)
print(len(final_list))
#[2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 197, 199, 311, 337, 373, 719, 733, 919, 971, 991, 1193, 1931, 3119, 3779, 7793, 7937, 9311, 9377, 11939, 19391, 19937, 37199, 39119, 71993, 91193, 93719, 93911, 99371, 193939, 199933, 319993, 331999, 391939, 393919, 919393, 933199, 939193, 939391, 993319, 999331]

# 55 YAY



#[1, 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 199, 311, 337, 373, 733, 919, 991]
#23 -1 = 22

#print(itertools)

#temp = list(itertools.permutations('12,1))
#print(temp)

#for x in itertools.permutations([0,1,2,3],4):
#  print(x)


