#!/usr/bin/env python3

# quesiton 30

#Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

#1634 = 14 + 64 + 34 + 44
#8208 = 84 + 24 + 04 + 84
#9474 = 94 + 44 + 74 + 44
#As 1 = 14 is not a sum it is not included.

#The sum of these numbers is 1634 + 8208 + 9474 = 19316.

#Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

#largest is 9^5x5? = 295245 stop at 1,000,000 to be safe

def power_sums(limit,expo):
  initial_list = []
  for i in range(2,limit):
    i_str = str(i)
    temp = 0
    #print(i_str)
    for char in i_str:
      #print('on char: ',char)
      if int(char)==0: temp+=0
      else:
        temp += int(char)**expo
        #print(' adding: ',int(char)**expo)
    if temp == i:
      initial_list.append(i)
  final_list = set(initial_list)
  return(final_list)

res = power_sums(1000000,5)
print(res,sum(res))
# 443839 YAY
