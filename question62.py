#!/usr/bin/env python3

# Cubic permutations
#Problem 62
#The cube, 41063625 (345^3), can be permuted to produce two other cubes: 56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

#Find the smallest cube for which exactly five permutations of its digits are cube.

# idea
# check for cubes using digital roots
# if digit root is not 0,1,8, it is not a cube
# inverse not true.


import time
start_time = time.time()


def make_cubes(start, limit):
  res = [0]*(limit-start+1)
  for i in range(len(res)):
    j = i+start
    res[i] = j*j*j
  return res



def is_permutation(num1,num2):
  str1 = "".join(sorted(str(num1)))
  return (str1 == "".join(sorted(str(num2))))

limit = 10000
start = 346

cubes = make_cubes(start,limit)

cube_count = [1]*len(cubes)
for i in range(len(cubes)):
  j=i+1
  while (j<len(cubes)):
    if is_permutation(cubes[i],cubes[j]):
      cube_count[i]+=1
      cube_count[j]+=1
    j+=1

for i in range(len(cube_count)):
  if cube_count[i] >= 5:
    print(cubes[i], cube_count[i])





print (' %s seconds ---' % (time.time()-start_time))

# 127035954683 5 YAY
#140283769536 5
#352045367981 5
#373559126408 5
#536178930624 5
#569310543872 5
#589323567104 5
#613258407936 5
#913237656408 5
#936302451687 5
# 159.55254745483398 seconds 




