#!/usr/bin/env python3

#Champernowne's constant
#Problem 40
#An irrational decimal fraction is created by concatenating the positive integers:

#0.123456789101112131415161718192021...

#It can be seen that the 12th digit of the fractional part is 1.

#If dn represents the nth digit of the fractional part, find the value of the following expression.

#d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

stop_at = [1,10,100,1000,10000,100000,1000000]

long_string='0'

for num in range(1,1000000):
  num_str=str(num)
  long_string += num_str  

result=1
for i in stop_at:
  result *= int(long_string[i])
    
print(len(long_string))
print(result)
#210 YAY

