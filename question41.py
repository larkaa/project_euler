#!/usr/bin/env python3

# Pandigital prime
#Problem 41
#We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

#What is the largest n-digit pandigital prime that exists?



# does not work. Check primality tests
# http://stackoverflow.com/questions/17298130/working-with-large-primes-in-python


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


## sieve of eratosthenes
# edited to give list of primes with max 9 digits
# need a better version for the large numbers:

import numpy
def primes_upto2(limit):
    is_prime = numpy.ones(limit + 1, dtype=numpy.bool)
    for n in range(2, int(limit**0.5 + 1.5)): 
        if is_prime[n]:
            is_prime[n*n::n] = 0
    return numpy.nonzero(is_prime)[0][2:]

def find_largest(primes):
  for p in reversed(primes):
    if is_pandigital(p):
      return p
  return 0

# print(is_pandigital(12345))

# find primes max of 9 digits
temp1 = primes_upto2(1000000000)
#temp1 = [y for y in candidate_list if y>100000000]
largest = find_largest(temp1)
print(largest)


