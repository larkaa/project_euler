#!/usr/bin/env python3

# quesiton 33 digit cancelling fractions
#The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

#We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

#There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

#If the product of these four fractions is given in its lowest common terms, find the value of the denominator.


# idea
# looking for fractions with one common digit that cancel
# so a1 / 1b OR a1/1b OR 1a/1b OR a1/b1 == a/b, where a and b in 1,9


a_list = [(0,0)]

for common in range(1,10):
  for a in range(1,10):
    if a != common:
     for b in range(1,10):
      if b!=common:
        if b!=a:
          temp_num = a*10+common
          temp_num2 = common*10 +a
          temp_div = b*10 + common
          temp_div2 = common*10 + b
          temp1 = temp_num/temp_div
          temp2 = temp_num/temp_div2
          temp3 = temp_num2/temp_div
          temp4 = temp_num2/temp_div2
          temp_list = [(temp_num,temp_div),(temp_num,temp_div2),(temp_num2,temp_div),(temp_num2,temp_div2)]
          temp_list_div = [temp1,temp2,temp3,temp4]
          if a/b in temp_list_div:
            a_list.append(temp_list[temp_list_div.index(a/b)])

print(a_list)
#[(0, 0), (16, 64), (26, 65), (64, 16), (65, 26), (19, 95), (49, 98), (95, 19), (98, 49)]
#[ (16, 64), (26, 65), (19, 95), (49, 98)]
# 1/4 2/5 1/5 1/2, product = 1/100



