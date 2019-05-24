#!/usr/bin/python


### question 7
#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see #that the 6th prime is 13.
#
#What is the 10 001 st prime number?

primes = [2,3,5,7,11,13]

def expand_prime_array(index):
  i=2+primes[-1]

  while len(primes)<index:
    
    if divides(i): 
      primes.append(i)
      i=i+1
    else: 
      i=i+1
    


def divides(num):
  for i in xrange(len(primes)):
     #print (i, primes[i]
     if num%primes[i]==0: 
        return 0
  return 1


#test = expand_prime_array(10001) # 
#print (primes[-1], len(primes))
#test = divides(100)
#print (test) # 

# question 10: sum of all primes below 2 million
def expand_prime_array2(num):
   i=1+primes[-1]
   while primes[-1]<(num-1):
     if divides(i):
       primes.append(i)
       i=i+1
     else:
       i=i+1

#print(sum(primes))
#expand_prime_array2(2000000)
#print(primes[-1])
#print(sum(primes))

## LONG EXECUTION TIME
# prime = 2000003  ## THIS is greater than 2million!
# sum = 142915828925
# --> 142913828922


## better idea to use a prime sieve,
## sieve of eratosthenes

def sum_primes(num):
  candidate_nums = [1]*num
  sum = 0
  #upper_lim = int(num**(.5))
  # indexes are the numbers themselves
  for i in xrange(2,num):
    if candidate_nums[i]:
      sum += i
      #print(i,sum)
      for j in xrange(i*i,num,i):
        candidate_nums[j] = 0
  return(sum)
      
print(sum_primes(2000000))
# 142913828922
# MUCH FASTER

## sieve of sundaram
# https://en.wikipedia.org/wiki/Sieve_of_Sundaram




