#!/usr/bin/env python3

# quesiton 31 integer right trianbles

#If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

#{20,48,52}, {24,45,51}, {30,40,50}

#For which value of p ≤ 1000, is the number of solutions maximised?

# idea - use pythagoreans theorem

# triangle inequality: longest side is shorter than the sum of the other two

# so choose a perimeter, then divide the digits in half. assign
# c to the smaller portion, then set a=1 and b=a-rest. 
# increase a and check.
# note can stop when a=b, because of symmetry

# ex: p=4 c=1, a=1, b=2, then

def is_right(a,b,c):
  if a*a+b*b==c*c: return 1
  else: return 0

def make_int_triangles(perimeter):
  response = []

  # start by defining the longest side
  c = perimeter//2
  if perimeter%2==0: c-=1
  a=1
  b=1
  #print(a,b,c)
  while (c>=1):
    for i in range(1,perimeter-c):
       a = i
       b = perimeter - c - a
       #print(a,b,c)
       if a<=b and b<=c and a+b>c:
         response.append((a,b,c))
       else:
          a=0
    c-= 1
  return(response)

# print(make_int_triangles(9))

def find_integer_rights(limit):
  response = [0]*(limit+1)
  a,b,c = (0,0,0)
  for p in range(3,limit+1):
    temp_sum=0
    candidates = make_int_triangles(p)
    for tri in candidates:
      a,b,c = tri
      temp_sum+= is_right(a,b,c)
    response[p] = temp_sum
  return(response)

temp = find_integer_rights(1000)
print('index :',temp.index(max(temp)) ,'triangles=',max(temp))
# index : 840 triangles= 8  YAY


