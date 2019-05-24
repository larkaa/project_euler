#!/usr/bin/env python3

# quesiton 26 reciprocal cycles
#A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

#1/2	= 	0.5
#1/3	= 	0.(3)
#1/4	= 	0.25
#1/5	= 	0.2
#1/6	= 	0.1(6)
#1/7	= 	0.(142857)
#1/8	= 	0.125
#1/9	= 	0.(1)
#1/10	= 	0.1
#Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

#Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

# from wikipedia
#A fraction in lowest terms with a prime denominator other than 2 or 5 (i.e. coprime to 10) always produces a repeating decimal. The length of the repetend (period of the repeating decimal) of 1/p is equal to the order of 10 modulo p. If 10 is a primitive root modulo p, the repetend length is equal to p − 1; if not, the repetend length is a factor of p − 1. This result can be deduced from Fermat's little theorem, which states that 10^(p−1) ≡ 1 (mod p).

# this only works for primitive primes mod

# so 2, 5 are out.
# easy: find the largest prime d <1000.

# find prime with limit num
## sieve of eratosthenes
def last_prime(num):
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

#temp = last_prime(1000)
#print(temp[-10:])
# 997 -- false!
# answer is 983
# didn't take into account beginning numbers...

# another way, using 

def cycle(n):
    myList = [1]
    t = 1
    f = (10**t) % n
    while myList.count(f) == 0:
        myList.append(f)
        t = t + 1
        f = (10**t) % n
    try:
        s = myList.index(f)
    except ValueError:
        s = 0
    return t-s

def solve():
    mx, val = 0, 0
    for n in range(2, 1000):
        m = cycle(n)
        if m > mx:
            mx = m
            val = n
    print('maximum cycle= ',mx, 'prime value= ',val)

solve()
