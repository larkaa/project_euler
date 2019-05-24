#!/usr/bin/env python3

#problem 24 lexicographic permutations

#A permutation is an ordered arrangement of objects. For example, 3124 is one #possible permutation of the digits 1, 2, 3 and 4. If all of the permutations #are listed numerically or alphabetically, we call it lexicographic order. The #lexicographic permutations of 0, 1 and 2 are:

#012   021   102   120   201   210

#What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, #5, 6, 7, 8 and 9?

# idea - find without calculating
# with 3 digits how does it go
#0123 0132 0213 0231 0312 0321 # 3! combos with 0, same with 1, 2, 3
#1023 1032

# 7th ?


# how big is 10! = 3 628 800
f10 = 3628800
f9 = 362880
f8 = 40320
f7 = 5040
f6 = 720
f5 = 120
f4 = 24
f3 = 6
f2= 2

factorials = [f10, f9,f8,f7,f6,f5,f4,f3,f2,1]


def find_first_fac(num):
  for j in range(len(factorials)):
    if factorials[j] < num:
      return j
  return 1

#i=0
#count = 8
#count = 1000000
#print(-len(numbers))
#factorials[-len(numbers)])

#print(fact_trim)


def num_iter(numbers, count):
  i=0
  final_array = []
  fact_temp = find_first_fac(factorials[-len(numbers)]) 
  fact_trim = factorials[fact_temp:]
  #print(numbers,fact_trim)
  for fact in fact_trim:
    # if divides evenly, keep number n-1, reverse the rest
    if count%fact==0:
      temp = count//fact
      final_array.append(numbers[temp-1])
      del numbers[temp-1]
      final_array.extend(numbers[::-1])
      return(final_array)
    # if factor too big, then lowest number is correct
    elif count < fact:
      final_array.append(numbers[0])
      del numbers[0]
      #print('  ',i, fact, count, numbers,final_array)

    # if count > fact, then the number of times
    # you divide is the index of the number we want
    else:
      #print('   ',i, count, fact, count//fact,numbers)
      temp = count//fact
      final_array.append(numbers[temp])
      del numbers[temp]
      #count -= temp*fact 
      #print(count,fact)
      #if temp%fact==0: temp = -(temp//fact-1)
      #print(temp,final_array,numbers)
      #final_array.append(numbers[temp])
      #del numbers[temp]
      count -= temp*fact 
    i+=1
  final_array.append(numbers[0])
  return(final_array) 

nums = [0,1,2,3,4,5,6,7,8,9]
#nums = [0,1,2,3]


#for i in range(1,13):
#  nums = [0,1,2,3]
#  print(i,num_iter(nums,i))

print(num_iter(nums,1000000))

# 2783915460  YAY

