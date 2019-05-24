#!/usr/bin/env python3

#question 21 amical numbers

# d(n) is the sum of the propor divisors of n
# if d(a) = b and d(b) = a, a!=b, then a and b are an amicable pair

# ex: d(220) = 284, d(284) = 220
# find sum of all amicable pairs under 10,000


class FactorCache:
    def __init__(self):
        self.cache = {}

    def __call__(self, n):
        if n == 1:
            return 1
        elif n in self.cache:
            return self.cache[n]
        else:
            c = self.__call__(all_factors(n))
            self.cache[n] = c
            return c + 1




def all_factors(num):
  total_factors = []
  i=1
  for j in range(1,num//2+1):
    if num%j==0:
      total_factors.append(j)
      i+=1
  return(total_factors)


# create list of sums of factors
sum_factors = [1]*10000
for i in range (2,10000):
  sum_factors[i] = sum(all_factors(i))

print(sum_factors[284])


# check which indices also exist
amical_pairs = []
for j in range (2,10000):
  a = sum_factors[j]
  if (a<10000 and a!=j and sum_factors[a] == j):
    amical_pairs.append(a)
    amical_pairs.append(j)

print(amical_pairs)
print(sum(amical_pairs)/2)
#  31626 YAY
# improvements = create a working cache of numbers?


#temp = all_factors(284)
#print(temp,sum(temp),sum(all_factors(220)))


