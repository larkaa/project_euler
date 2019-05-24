#!/usr/bin/env python3

import numpy as np
import operator as op
from functools import reduce

#Maximum path sum II
#Problem 67
#By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

#3
#7 4
#2 4 6
#8 5 9 3

#That is, 3 + 7 + 4 + 9 = 23.

#Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.

#NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, as there are 299 altogether! If you could check one trillion (1012) routes every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)



filename = 'p067_triangle.txt'
rawfile = open(filename).read()


# split by line
lines = rawfile.splitlines()


# create matrix to hold data
grid_n = np.zeros(shape=(len(lines),len(lines)))


# convert to integers
for i in range(len(lines)):
  num_str = lines[i]
  nums = np.asarray(num_str.split(' '))
  grid_n[i,:len(nums)] = nums


print(grid_n[0:3,:])
#print(grid_n[0:3,:])

def walk_sum(grid,row,col):
  if row==0: return grid[0,0]
  if (row>0):
    if(col>0):
      temp1=grid[row-1,col]
      temp2=grid[row-1,col-1]
      if temp1>temp2:
        return(grid[row,col]+walk_sum(grid,row-1,col))
      return(grid[row,col]+walk_sum(grid,row-1,col-1))
    return(grid[row,col]+walk_sum(grid,row-1,col))


count = 0
#print(grid_n.shape)
#for i in range(grid_n.shape[1]):
#  temp = walk_sum(grid_n,grid_n.shape[0]-1,i)
#  if temp > count: count = temp

#print(count)

# idea 2 - optimal substructure!
# start from top, and calculate max sum for each element
# at the bottom, take the max

def max_sum(grid):
  grid_sum = np.zeros(shape=(grid.shape[0],grid.shape[1]))
  
  for row in range(0,grid.shape[0]):
    for col in range(0,row+1):
      #print(row,col, grid[row,col])
      grid_sum[row,col] = grid[row,col]
      if row==0: 
        if col==0: grid_sum[0,0] = grid[0,0]      
        else: grid_sum[row,col] += grid_sum[row-1,col]
        #print("row 0,", row,grid[row-1,col],grid_sum[row,col])
      elif col==row:
        grid_sum[row,col] += grid_sum[row-1,col-1]
        #print("col=row,", row,grid[row-1,col-1],grid_sum[row,col])
      else: 
        grid_sum[row,col] += max([grid_sum[row-1,col-1],grid_sum[row-1,col]])
  return(grid_sum)


temp = max_sum(grid_n)
print(temp[-1,:],max(temp[-1,:]))

# 7273 YAY





