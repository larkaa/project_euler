#!/usr/bin/python

num = 600851475143
#num = 12

#crappy method
def isprime(n):
  j=1
  for i in xrange(2,n-1):
     if not(n%i):
        j=0 
        break
  return[j]




#method 1
def largest_prime_factor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n


print '%r' %(largest_prime_factor(num))

#method 2
n = 600851475143
i = 2
while i * i < n:
     while n % i == 0:
         n = n / i
     i = i + 1

print (n)

#print '%r' %(isprime(3) )
