#!/usr/bin/env python3

# quesiton 31 coin sums
#In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

#1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
#It is possible to make £2 in the following way:

#1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
#How many different ways can £2 be made using any number of coins?

# idea - use recursive programming
def countChange(money, coins):
  if money==0:
    return 1
  elif len(coins)==0 or money<0:
    return 0
  else: return(countChange(money - coins[0], coins) + countChange(money, coins[1:]))



coins = [200,100,50,20,10,5,2,1]
print(countChange(200,coins))
# 73682 YAY




