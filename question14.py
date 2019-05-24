#!/usr/bin/env python3

#question 14 largest collatz sequence
# n-> n/2 if even
# n -> 2n+1 if odd

# Which starting number, under one million, produces the longest chain?



def next(num):
  if num%2: return (3*num+1)
  return (num//2)

class ChainCache:
    def __init__(self):
        self.cache = {}

    def __call__(self, n):
        if n == 1:
            return 1
        elif n in self.cache:
            return self.cache[n]
        else:
            c = self.__call__(next(n))
            self.cache[n] = c + 1
            return c + 1


chainlen = ChainCache()

def maxlen(x):
  m = 0
  v = 0
  for i in range(1,x):
    l = chainlen(i)
    if l>m:
      m = l
      v = i
  return v,m

temp = maxlen(1000000)
print (temp)

#(837799, 525)



