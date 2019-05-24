#!/usr/bin/python

##question 4: Find the largest palindrome made from the product of two 3-digit numbers

#number must be lower than 999*999 = 998001
#number must be greater than 100*100 = 10000
# implies palindromes of 5 or 6 digits
# there are 10*9=90 5-digit palindromes
# there are 9*10*10=900 6-digit palindromes
# suffice to create palindromes then check?


maximum = 998001
minimum = 10000

# not needed
#def is_palin(num):
#  return str(num) == str(num)[::-1]
#print '%r' %(is_palin(1010))

#check if prodcut of two 3-digit numbers
def product3(num):
  j=0
  for i in xrange(999,100,-1):
    if(num%i==0):
      j=num/i
      if(len(str(j))==3):
         #print(num, i, j) 
         return(i,j)
  return(0)


#check 6-digit palindromes


for a in xrange(9,0,-1):
  for b in xrange(9,-1,-1):
    for c in xrange(9,-1,-1):
     num = int(str(a)+str(b)+str(c)+str(c)+str(b)+str(a)) 
     temp = product3(num)
     if temp !=0:
       print(num, temp) 
       break;

# answer = 906609
#(True, 906609, (993, 913))

# with incorrect code=888888

# above 888888?
#xrange ending is ending -1
#for a in xrange(9,7,-1):
#  for b in xrange(9,-1,-1):
#    for c in xrange(9,-1,-1):
#     num = int(str(a)+str(b)+str(c)+str(c)+str(b)+str(a)) 
#     temp = product3(num)
#     print(num, temp)
#     if temp !=0:
#       print(True, num, temp) 
#       break;


# more comments
#The palindrome can be written as:

#abccba

#Which then simpifies to:

#100000a + 10000b + 1000c + 100c + 10b + a

#And then:

#100001a + 10010b + 1100c

#Factoring out 11, you get:

#11(9091a + 910b + 100c)




