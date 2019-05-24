#!/usr/bin/env python3

#question 15 lattice paths

#Starting in the top left corner of a 2×2 grid, and only being 
#able to move to the right and down, there are exactly 6 routes 
#to the bottom right corner.


#How many such routes are there through a 20×20 grid?


# idea
# for 2,2 grid, you must go down 2 and right twice,
# this is all possible combinations of DDRR
# there are 4 choose 2, or 6
# this counts the number of a objects out of a+b, or 
# for 20x20 grid, there are 40 choose 20 or 
# 40 nCr 20 = 137846528820

def countRoutes(n):
  result = 1
  for i in range(1,n+1):
    result = result*(n+i)/i
  return(result)

print(countRoutes(20))
