#!/usr/bin/env python3


# Resilience
#Problem 243
#A positive fraction whose numerator is less than its denominator is called a proper fraction.
#For any denominator, d, there will be d−1 proper fractions; for example, with d = 12:
#1/12 , 2/12 , 3/12 , 4/12 , 5/12 , 6/12 , 7/12 , 8/12 , 9/12 , 10/12 , 11/12 .

#We shall call a fraction that cannot be cancelled down a resilient fraction.
#Furthermore we shall define the resilience of a denominator, R(d), to be the ratio of its proper fractions that are resilient; for example, R(12) = 4/11 .
#In fact, d = 12 is the smallest denominator having a resilience R(d) < 4/10 .

#Find the smallest denominator d, having a resilience R(d) < 15499/94744 .


# this needs euliers totient function

import math
import random
import time
s1=time.time()

#perform a Modular exponentiation
def modular_pow(base, exponent, modulus):
    result=1
    while exponent>0:
        if exponent%2==1:
           result=(result * base)%modulus
        exponent=exponent>>1
        base=(base * base)%modulus
    return result

#Miller-Rabin primality test
def checkMillerRabin(n,k):
    if n==2: return True
    if n==1 or n%2==0: return False

    #find s and d, with d odd
    s=0
    d=n-1
    while(d%2==0):
        d/=2
        s+=1
    assert (2**s*d==n-1)

    #witness loop
    composite=1
    for i in range(k):
        a=random.randint(2,n-1)
        x=modular_pow(a,d,n)
        if x==1 or x==n-1: continue
        for j in range(s-1):
            composite=1
            x=modular_pow(x,2,n)
            if x==1: return False #is composite
            if x==n-1: 
                composite=0
                break
        if composite==1:
            return False        #is composite
    return True                 #is probably prime

def findPrimes(n):              #generate a list of primes, using the sieve of eratosthenes

    primes=(n+2)*[True]

    for i in range(2,int(math.sqrt(n))+1):
        if primes[i]==True:
            for j in range(i**2,n+1,i):
                primes[j]=False

    primes=[i for i in range(2,len(primes)-1) if primes[i]==True]
    return primes

def primeFactorization(n,primes):   #find the factors of a number

    factors=[]

    i=0
    while(n!=1):
        if(n%primes[i]==0):
            factors.append(primes[i])
            n/=primes[i]
        else:
            i+=1

    return factors

def phi(n,primes):
    #some useful properties
    if (checkMillerRabin(n,10)==True):      #fast prime check
        return n-1

    factors=primeFactorization(n,primes)    #prime factors
    distinctive_prime_factors=set(factors)  

    totient=n
    for f in distinctive_prime_factors:     #phi = n * sum (1 - 1/p), p is a distinctive prime factor
        totient*=(1-1.0/f);

    return totient

if __name__ == '__main__':


    s=0
    N=165975
    # N=430000
    primes=findPrimes(N)    #upper bound for the number of primes
    limit = 15499/94744

    for i in range(1,N):
        a=phi(i,primes)

        s+=a
        if (i-a-1)/i < limit:
          print(i, i-a-1)

    print("Sum =",s )

#limit = 15499/94744
#a=True
#i=12
#while a:
#  #for i in range(len(a)):
#  s = phi(i)
#  if (i-phi(i)-1)/i < limit:
#    print(i-phi(i)-1,i); a=False
#  i+=1


print("{}s".format(time.time() - s1))


# 





