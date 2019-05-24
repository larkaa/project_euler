#!/usr/bin/env python3

import numpy as np
import operator as op
from functools import reduce

#question 18 triangle sum

#By starting at the top of the triangle below and 
#moving to adjacent numbers on the row below, the 
#maximum total from top to bottom is 23.
#3
#7 4
#2 4 6
#8 5 9 3

#That is, 3 + 7 + 4 + 9 = 23.
#Find the maximum total from top to bottom of the triangle below:

grid='''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
'''

# idea. start from end and check at each step the max value
# then check sums of possible routes, keep max
# didn't work :-(




# convert string to matrix
lines = grid.splitlines()

# create matrix to hold data
grid_n = np.zeros(shape=(len(lines),len(lines)))


for i in range(len(lines)):
  num_str = lines[i]
  nums = np.asarray(num_str.split(' '))
  grid_n[i,:len(nums)] = nums

#print(grid_n)

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


#temp = max_sum(grid_n)
#print(temp,temp[-1,:],max(temp[-1,:]))

# 1074 YAY



#question 17
# count the number of letters in the numbers 1 to 1000
# format
# one hundred and thirty one

digits_str = ['one','two','three','four','five','six','seven','eight','nine']
teens_str = ['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
twenty_plus_str = ['twenty','thirty','fourty','fifty','sixty','seventy','eighty','ninety']

 
digits = [len(x) for x in digits_str]
teens = [len(x) for x in teens_str]
tens =  [len(x) for x in twenty_plus_str]
hundred = 7
hundred_and = 10
# X hundred *(1+(3+ninty nine others))
one_thou = len('onethousand')

total_sum = 0

# digits and teens
total_sum+= sum(digits) + sum(teens)

# tens are in the form twenty, thrity, then 
#  twenty-one two...nine, thirty-one two... nine,
# = twenty appears 9 times more
# but the number one appears 8 times more for each twenty, 
# so 8*9

total_sum += 9*(sum(tens) + 8*sum(digits))
sumto99 = total_sum

# hundreds are of the form 
# one hundred, two, three... nine
# one hundred AND one... ninety nine... nine hundred AND one... ninety nine
# -> hundred appears nine times more digits one time
# -> sumto99 appears 9 times more + hundred_and *90 (less 9 bc not including 100,200,300)


total_sum += 9*(hundred + sum(digits))
total_sum += 9*sumto99 + 90*hundred_and

# one thousand once
total_sum += one_thou

print(total_sum)

#sum_to_99 = sum(digits) + sum(teens) + sum(tens) + sum(tens)*sum(digits)

#total_num_sum = sum_to_99+ sum(hundreds[0]*digits)+sum([x*sum_to_99 for x in hundreds])*sum(digits)


#print([x*sum_to_99 for x in hundreds if x>7])
#print(sum_to_99,total_num_sum)



