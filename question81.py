#!/usr/bin/env python3


#Path sum: two ways
#Problem 81
#In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by only moving to the right and down, is indicated in bold red and is equal to 2427.


#Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing a 80 by 80 matrix, from the top left to the bottom right by only moving right and down.

import numpy as np
import operator as op
from functools import reduce
import csv
import time
start_time = time.time()

# read file
filename = 'p081_matrix.txt'
rawfile = open(filename).read()


# split by line
lines = rawfile.splitlines()

# create matrix to hold data
grid_n = np.zeros(shape=(len(lines),len(lines)))

# convert to integers
for i in range(len(lines)):
  num_str = lines[i]
  nums = np.asarray(num_str.split(','))
  grid_n[i,:len(nums)] = nums

#print(grid_n)
#print(sum(grid_n[0,:]))


# idea - this is dijkstras algorithm!
# can use modified version as can only go down and right

def dijkstra(grid):
  grid_paths = np.zeros(shape=(grid.shape[0],grid.shape[1]))
  maxrow = grid.shape[0]
  maxcol = grid.shape[1]

  #initialize first row
  #grid_paths[0,0]=grid[0,0]
  for i in range(0,maxcol):
    grid_paths[0,i] = sum(grid[0,0:i+1])

  for row in range(1,maxrow):
    for col in range(0,maxcol):
      if col==0:
        grid_paths[row,col] = grid[row,col]+grid_paths[row-1,col]
      else:
        grid_paths[row,col] = grid[row,col] + min(grid_paths[row-1,col],grid_paths[row,col-1])
  #print(grid_paths)
  return(grid_paths[maxrow-1,maxcol-1])

t=dijkstra(grid_n)
print(t)

print ('%s seconds ---' % (time.time()-start_time))

# 427337.0 YAY
# 0.01434469223022461 seconds ---





