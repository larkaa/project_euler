#!/usr/bin/env python3

# quesiton 25: index of first fib number with over 1000 digits?
# ex: index of first fib with over 2 digits is F12 = 144

def fib_digits(digits):
  fib = [1,1] #fib1 et 2
  temp = 1
  while len(str(fib[-1])) < digits:
    fib.append(fib[-1]+fib[-2])
  return(len(fib),fib[-1])

print(fib_digits(1000))
