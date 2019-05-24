#!/usr/bin/env python3

# quesiton 45: triangular, pentagonal, hexagonal


def triangular(n):
  return n*(n+1)/2

def pentagonal(n):
  return n*(3*n-1)/2

def hexagonal(n):
  return n*(2*n-1)

# first sequence is t285 = p165 = h143
# start with these values and up to others

# initialize

# idea, keep only triangle numbers
# plus list of penta and hex numbers
# check one by one, then iterate the triangles



def find_common(start):
  a=0

  pen_list = []
  hex_list = []
  for j in range(1,start):
    pen_list.append(pentagonal(j))

  for k in range(1,start):  
    hex_list.append(hexagonal(k))

  while a==0:
    tri_num = triangular(start)
    if  tri_num in hex_list and tri_num in pen_list:
      return tri_num

    else: 
      start+=1
      pen_list.append(pentagonal(start))
      hex_list.append(hexagonal(start))

#print(find_common(286))
# 1533776805

# more optimized. all hexigonal numbers are triangular, so only need
# to check pentagonal numbers
# note that p = n(3n-1)/2 = 3n^2-n-2p
# replace p with a hexagon number

# quadratic formula, x = (1 +- sqrt(1-4*3*(-2))/2*3
# = (1 + sqrt(1+24*h))/6

import math
n=1
res_list = [0]
while res_list[-1]<=40755 :
  n += 1
  h = n*(2*n-1)
  k = (1 + math.sqrt(1+24*h))/6
  if k == int(k):
    res_list.append(h)

print(res_list)
# [0, 40755, 1533776805]






