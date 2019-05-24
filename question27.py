#!/usr/bin/env python3

# quesiton 26 quadratic primes
#Euler discovered the remarkable quadratic formula:

#n2+n+41n2+n+41
#It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤390≤n≤39. However, when n=40,402+40+41=40(40+1)+41n=40,402+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,412+41+41n=41,412+41+41 is clearly divisible by 41.

#The incredible formula n2−79n+1601n2−79n+1601 was discovered, which produces 80 primes for the consecutive values 0≤n≤790≤n≤79. The product of the coefficients, −79 and 1601, is −126479.

#Considering quadratics of the form:

#n2+an+bn2+an+b, where |a|<1000|a|<1000 and |b|≤1000|b|≤1000

#where |n||n| is the modulus/absolute value of nn
#e.g. |11|=11|11|=11 and |−4|=4|−4|=4
#Find the product of the coefficients, aa and bb, for the quadratic expression that produces the maximum number of primes for consecutive values of nn, starting with n=0n=0.

# idea
# note that a and b are both prime and relatively prime
# find list of primes <=1000, then alternate through them with their
# postivie and negative values


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
  return(res)
      
#print(list_primes(1001))

primes = list_primes(1000000)

#function to calculate value
def quadratic(a,b,n):
  return (n*n + a*n + b)

def prime_series_length(a,b):
  n=0
  z=1
  while z:
    temp = quadratic(a,b,n)
    #print(temp)
    if temp not in primes:
      return(n); z=0
    n+=1

#print(prime_series_length(-79,1601)) # 80

res = (0,0,0) #a,b,length

ab_candidates = [-y for y in primes if y < 1001]
ab_candidates = ab_candidates + [y for y in primes if y < 1001]

temp = 0
for num1 in ab_candidates:
  for num2 in ab_candidates:
    if num1==num2:
      temp=0
    else:
      temp = prime_series_length(num1,num2)
      if temp>res[2]:
        res = (num1,num2,temp)

print(res)
# (-61, 971, 71) YAY






#loop through pos and negative elements






