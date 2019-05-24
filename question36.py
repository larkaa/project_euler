#!/usr/bin/env python3

# quesiton 36 double-base palindromes
#The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

#Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

#(Please note that the palindromic number, in either base, may not include leading zeros.)

def is_palindrome(num):
  temp1 = str(num)
  temp2=''
  limit = len(temp1)
  for i in range(limit):
    #print(i,temp1,temp2,limit)
    temp2 += temp1[limit-i-1]
  if int(temp1)==int(temp2):
    return(1)
  return(0)

#print(is_palindrome(101))
#print(is_palindrome(1012))

def make_palindrome(limit):
  final_list = [1,2,3,4,5,6,7,8,9]
  # add all single digits

  for i in range(len(str(limit))//2):
    for j in range(10**i,10**(i+1)):
      temp = str(j) + str(j)[::-1]
      final_list.append(int(temp))
      for z in range(10):
        temp = str(j) + str(z)+ str(j)[::-1]
        final_list.append(int(temp))
  #clean up repeats
  final_list = set(final_list)
  final_list = [y for y in final_list if y<limit]
  return(final_list)


def brute_palindrome(limit):
  final_list = []
  for i in range(1,limit):
    if is_palindrome(i):
      final_list.append(i)
  return(final_list)

candidates = make_palindrome(1000000)
#candidates = brute_palindrome(1000000) 
#for test in candidates:
#  t = is_palindrome(test)
#  if t==0:
#    print("failed: ",test)
#    break;

#print(format(101,'b'))

final_answer = []
for num in candidates:
    #if num<1000000:
    if is_palindrome(format(num,'b')):
      final_answer.append(num)
      #final_answer.append((num,format(num,'b')))

print(final_answer)
print(sum(final_answer))
# 25846843 - double counting of palindromes
# 872187 YAY ! (one is included)

